from web3 import Web3
import json

url = "http://143.215.130.235:8545"

web3 = Web3(Web3.HTTPProvider(url))
print(web3.isConnected())

def getTransactions(start, end, address, dir):
    print(f"Searching through block number {start} to {end} for transactions involving the address {address}")
    tx_hashes = []
    for i in range(start, end):
        block = web3.eth.getBlock(i, full_transactions=True)
        for tx in block.transactions:
            if tx['to'] == address or tx['from'] == address:
                tx_hashes.append(tx['hash'].hex())
    print(f"Finished searching blocks {start} through {end} and found {len(tx_hashes)} transactions")

    with open(dir, 'w') as f:
        json.dump(tx_hashes, f, indent=2)

address = "0x2a48DB21c691cf26fF12Df84476125F51824b909"
end_block = web3.eth.blockNumber
start_block = 276276 # first block with tx to Buzzcoin contract according to block explorer
target_dir = "transactions.json"
getTransactions(start_block, end_block, address, target_dir)
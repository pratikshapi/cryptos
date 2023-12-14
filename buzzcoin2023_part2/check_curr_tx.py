from web3 import Web3
import json

url = "http://143.215.130.235:8545"

web3 = Web3(Web3.HTTPProvider(url))
print(web3.isConnected())

def getTransactions(start):
    tx_hashes = []
    for i in range(start, start+1):
        block = web3.eth.getBlock(i, full_transactions=True)
        for tx in block.transactions:
            print(tx)

address = "0x2a48DB21c691cf26fF12Df84476125F51824b909"
end_block = web3.eth.blockNumber
start_block = 276276 # first block with tx to Buzzcoin contract according to block explorer
getTransactions(start_block)
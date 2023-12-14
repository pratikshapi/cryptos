'''
run web3 transactions
'''

from web3 import Web3
import time
from eth_abi import encode_abi, decode_abi
from Crypto.Hash import keccak

web3 = Web3(Web3.HTTPProvider('http://143.215.130.235:8545'))
abi = [
    {
        "inputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "payable": True,
        "stateMutability": "payable",
        "type": "fallback"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "KOTH_coup",
        "outputs": [
            {
                "internalType": "bool",
                "name": "",
                "type": "bool"
            }
        ],
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "KOTH_withdraw",
        "outputs": [],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "coup_block",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "donate",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "duel1v1",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "duel_highroller",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "nonce",
                "type": "uint256"
            }
        ],
        "name": "guess_the_number",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [],
        "name": "mayor_voting",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "most_sent",
        "outputs": [
            {
                "internalType": "uint256",
                "name": "",
                "type": "uint256"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": False,
        "inputs": [
            {
                "internalType": "uint256",
                "name": "nonce",
                "type": "uint256"
            },
            {
                "internalType": "uint256",
                "name": "d",
                "type": "uint256"
            }
        ],
        "name": "pay_to_mine",
        "outputs": [],
        "payable": True,
        "stateMutability": "payable",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "richest",
        "outputs": [
            {
                "internalType": "address payable",
                "name": "",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

myContract = web3.eth.contract(address=('0x3CacA428df17dC6E8C2700aac77b3C261A12cFd9'), abi=abi)
myAdress = "0x2a48DB21c691cf26fF12Df84476125F51824b909"
redundancy = 4
gas_price = web3.eth.gas_price
with open('private_key.pem', 'rb') as f:
    private_key = f.read().strip().decode('utf-8')
    private_key = "0x" + private_key

def getNonce(myAdress):
    print(f"getting nonce for: {myAdress}")
    return web3.eth.get_transaction_count(
        Web3.toChecksumAddress(myAdress)
    )

def signTx(transaction, private_key):
    signed = web3.eth.account.sign_transaction(transaction, private_key)
    return signed

def sendTx(signedTx):
    print(f"Sending transaction: {signedTx.rawTransaction.hex()}")
    count = 0

    for i in range(redundancy):
        try:
            web3.eth.send_raw_transaction(signedTx.rawTransaction)
            return True
        except Exception as e:
            print(f"Error: {e}")
            count += 1
            time.sleep(1)
    if count == 4:
        print("Failed to send transaction")
    
    
    return False

def getHash(signedTx):
    print(f"getting hash: {signedTx.hash.hex()}")
    return web3.toHex(web3.keccak(signedTx.rawTransaction))

def checkHash(hash):
    print(f"Checking hash: {hash}")
    return web3.eth.getTransactionReceipt(hash)


def run_transaction(run=False, nonce=None):
    if run == False:
        return

    # get the nonce
    address_nonce = getNonce(myAdress)

    # construct the transaction
    transaction = myContract.functions.guess_the_number(
        nonce
        ).buildTransaction({
            'value': web3.toWei(1, 'ether'),
            'chainId': 9090,
            'gas': 1000000,
            'gasPrice': gas_price,
            'nonce': address_nonce
        })
    
    # sign the transaction
    signedTx = signTx(transaction, private_key)
    sendTx(signedTx)

    time.sleep(6)
    # check if the transaction was successful
    # hash = getHash(signedTx)
    # receipt = checkHash(hash)
    # print(receipt)


def get_temp_value(arg_types,arg_values):
    encoded_args = encode_abi(arg_types, arg_values)
    hash_obj = keccak.new(digest_bits=256)
    hash_obj.update(encoded_args)
    temp = hash_obj.hexdigest()
    temp = int(temp, 16)
    return temp

def guess_the_number_util(nonce):
    assert nonce <= 100
    
    # use user address to get a temp value
    arg_types = ['address']
    arg_values = [myAdress]
    temp = get_temp_value(arg_types, arg_values)

    # use temp value and block number to get a temp value
    arg_types = ['uint256', 'uint256']
    arg_values = [temp, (web3.eth.blockNumber + 1)]
    temp = get_temp_value(arg_types, arg_values)

    # use temp value and temp value to get a temp value
    arg_types = ['uint256', 'uint256']
    arg_values = [temp, temp]
    temp = get_temp_value(arg_types, arg_values)

    temp = temp % 100

    if nonce == temp:
        print(nonce)
        run_transaction(True, nonce)

def guess_the_number():
    for i in range(100):
        # Get the current block number
        guess_the_number_util(i)



guess_the_number()

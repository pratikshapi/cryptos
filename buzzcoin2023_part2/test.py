'''
run web3 transactions
'''

from web3 import Web3
import time
import hashlib
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

myContract = web3.eth.contract(address='0x3CacA428df17dC6E8C2700aac77b3C261A12cFd9', abi=abi)
myAdress = "0x2a48DB21c691cf26fF12Df84476125F51824b909"
redundancy = 4
gas_price = web3.eth.gas_price
with open('private_key.pem', 'rb') as f:
    private_key = f.read().strip().decode('utf-8')
    private_key = "0x" + private_key


# Get the current block number
block_number = web3.eth.block_number
print(block_number)


'''
assert(nonce <= 100);
uint256 temp = uint256(keccak256(abi.encode(msg.sender)));
temp = uint256(keccak256(abi.encode(temp, block.number)));
temp = uint256(keccak256(abi.encode(temp, temp)));
temp = temp % 100;
'''

def get_temp_value(arg_types,arg_values):
    encoded_args = encode_abi(arg_types, arg_values)
    hash_obj = keccak.new(digest_bits=256)
    hash_obj.update(encoded_args)
    temp = hash_obj.hexdigest()
    temp = int(temp, 16)
    return temp

def guess_the_number(nonce):
    assert nonce <= 100
    
    # use user address to get a temp value
    arg_types = ['address']
    arg_values = [myAdress]
    temp = get_temp_value(arg_types, arg_values)

    # use temp value and block number to get a temp value
    arg_types = ['uint256', 'uint256']
    arg_values = [temp, web3.eth.blockNumber]
    temp = get_temp_value(arg_types, arg_values)

    # use temp value and temp value to get a temp value
    arg_types = ['uint256', 'uint256']
    arg_values = [temp, temp]
    temp = get_temp_value(arg_types, arg_values)

    temp = temp % 100

    if nonce == temp:
        print(nonce)


for i in range(100):
    guess_the_number(i)
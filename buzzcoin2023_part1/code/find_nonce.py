from web3 import Web3
from eth_abi import encode_abi


# Connect to the Ethereum network using Web3
web3 = Web3(Web3.HTTPProvider('http://143.215.130.235:8545'))

# Address to query for transactions
address = '0x4E4a885a977AEA351D8bE069d41c548C08c2C6c6'.lower()

address = Web3.toChecksumAddress(address)

# Get the transaction count (nonce) for the address
total_tx = web3.eth.get_transaction_count(address)

# Iterate through all transactions from the address

blocks = [0x6229, 0x6289, 0x62a1, 0x62da, 0x63b3, 0x63b7, 0x63c0, 0x63c1, 0x63c1, 0x63c5, 0x63c9, 0x63d3, 0x63de, 0x6499, 0x649b, 0x649d, 0x7345, 0x7353, 0x799b, 0x79a3, 0x79a5, 0x79a9, 0x79aa, 0x79ab, 0x79ae, 0x79ae, 0x79ae, 0x79ae, 0x79af, 0x79af, 0x79af, 0x79b1, 0x79b2, 0x79b3, 0x79b3, 0x79b3, 0x79b4, 0x79b4, 0x79b4, 0x79b4, 0x79b5, 0x79b5, 0x79b5, 0x79b5, 0x79b5, 0x79b5, 0x79b5, 0x79b6, 0x79b6, 0x79b6, 0x79b6, 0x79b7, 0x79b7, 0x79b8, 0x79b8, 0x79b9, 0x79b9, 0x79ba, 0x79bc, 0x79bd, 0x79bd, 0x79bd, 0x79bd, 0x79be, 0x79be, 0x79be, 0x79be, 0x79be, 0x79bf, 0x79c2, 0x79c2, 0x79c2, 0x79c2, 0x79c2, 0x79c2, 0x79c2, 0x79c2, 0x79c2, 0x79c3, 0x79c3, 0x79c4, 0x79c5, 0x79c5, 0x79c8, 0x79ca, 0x79cb, 0x79cb, 0x79cc, 0x79cc, 0x79cc, 0x79cc, 0x79cc, 0x79cc, 0x7ac0, 0x19853, 0x19c21, 0x19c44, 0x19c58, 0x19d17, 0x19ea4, 0x19eb0, 0x19eb8, 0x19ebc, 0x19ec8, 0x19eca, 0x19ecc, 0x19ed6, 0x19eee, 0x19ef0, 0x19eff, 0x19f09, 0x19f0e, 0x19f11, 0x19f13, 0x19f1e, 0x19f1e, 0x19f1e, 0x19f21, 0x19f2c, 0x19f5d, 0x19f5e, 0x19f61, 0x19f66, 0x19f68, 0x19f68, 0x19f6c, 0x19f70, 0x19f71, 0x19f75, 0x19f77, 0x19f7a, 0x19f7b, 0x19f80, 0x19f81, 0x19f88, 0x19f96, 0x19f97, 0x19f9b, 0x19f9f, 0x19f9f, 0x19fa1, 0x19fa4, 0x19fb5, 0x19fd3, 0x1a008, 0x1a00e, 0x1a011, 0x1a014, 0x1a01d, 0x1a02a, 0x1a031, 0x1a044, 0x1a052, 0x1a055, 0x1a056, 0x1a057, 0x1a05b, 0x1a05e, 0x1a05e, 0x1a05f, 0x1a05f, 0x1a061, 0x1a062, 0x1a064, 0x1a064, 0x1a064, 0x1a064, 0x1a065, 0x1a065, 0x1a065, 0x1a065, 0x1a069, 0x1a08d, 0x1a08d, 0x1a09f, 0x1a0b0, 0x1a0ba, 0x1a0bf, 0x1a0ed, 0x1a0f0, 0x1a0f5, 0x1a0f7, 0x1a0fb, 0x1a0fe, 0x1a102, 0x1a102, 0x1a105, 0x1a107, 0x1a111, 0x1a114, 0x1a114, 0x1a114, 0x1a11a, 0x1a11b, 0x1a11b, 0x1a11d, 0x1a11e, 0x1a11f, 0x1a127, 0x1a127, 0x1a127, 0x1a127, 0x1a128, 0x1a128, 0x1a128, 0x1a128, 0x1a134, 0x1a134, 0x1a13f, 0x1a14a, 0x1a151, 0x1a154, 0x1a155, 0x1a15d, 0x1a16c, 0x1a173, 0x1a173, 0x1a173, 0x1a17d, 0x1a197, 0x1a1a7, 0x1a1aa, 0x1a1b7, 0x1a1b9, 0x1a1ba, 0x1a1bd, 0x1a1bd, 0x1a1be, 0x1a2da, 0x1a2e1, 0x1a2e7, 0x1a2e7, 0x1a323, 0x1a327, 0x1a398, 0x1a398, 0x1a3a2, 0x1a3ca, 0x1a3cf, 0x1a3d2, 0x1a44c, 0x1a44e, 0x1a452, 0x1a487, 0x1a48a, 0x1a493, 0x1a495, 0x1a497, 0x1a49a, 0x1a49c, 0x1a4ce, 0x1a4d4, 0x1a4db, 0x1a4f1, 0x1a4fd, 0x1a4fd, 0x1a501, 0x1a501, 0x1a501, 0x1a501, 0x1a503, 0x1a504, 0x1a510, 0x1a51c, 0x1a527, 0x1a527, 0x1a527, 0x1a527, 0x1a528, 0x1a52a, 0x1a53f, 0x1a549, 0x1a557, 0x1a5df, 0x1a623, 0x1a62e, 0x1a633, 0x1a63e, 0x1a646, 0x1a652, 0x1a652, 0x1a657, 0x1a65a, 0x1a65c, 0x1a660, 0x1a663, 0x1a664, 0x1a665, 0x1a666, 0x1a667, 0x1a668, 0x1a6db, 0x1a6de, 0x1a6de, 0x1a6de, 0x1a6de, 0x1a6de, 0x1a6de, 0x1a6de, 0x1a6de, 0x1a6e7, 0x1a6ea, 0x1a6ea, 0x1a6fc, 0x1a703, 0x1a706, 0x1a708, 0x1a709, 0x1a70c, 0x1a70d, 0x1a76a, 0x1a7a1, 0x1a7d7, 0x1a7f6, 0x1a8e3, 0x1a914, 0x1a998, 0x1a9c7, 0x1aa4d, 0x1ab07, 0x1aba2, 0x1abd6, 0x1abef, 0x1ac66, 0x1ac69, 0x1b4ff, 0x1b516, 0x1b52d, 0x1b53a, 0x1b540, 0x1b542, 0x1b655, 0x1b69d, 0x1b6aa, 0x1b71e, 0x1b735, 0x1b73d, 0x1b74a, 0x1b750, 0x1b75b, 0x1b781, 0x1b795, 0x1b79f, 0x1b7b6, 0x1b7b7, 0x1b7b8, 0x1b7b9, 0x1b7ba, 0x1b7bb, 0x1b7bc, 0x1b7bd, 0x1b7be, 0x1b7c0, 0x1b7c1, 0x1b7d1, 0x1b7d2, 0x1b7d3, 0x1b7d5, 0x1b7d6, 0x1b7d7, 0x1b7d8, 0x1b7d9, 0x1b7da, 0x1b7db, 0x1b7dc, 0x1b7de, 0x1b7e0, 0x1b7e1, 0x1b7e2, 0x1b7e3, 0x1b7e4, 0x1b7e5, 0x1b7e6, 0x1b7fa, 0x1b806, 0x1b825, 0x1b832, 0x1b84f, 0x1b85b, 0x1b891, 0x1b89d, 0x1b8ad, 0x1b8d3, 0x1b8df, 0x1b8e9, 0x1b8eb, 0x1b8ee, 0x1b8f0, 0x1b923, 0x1b92a, 0x1b968, 0x1b96c, 0x1baa1, 0x1baa4, 0x1baaa, 0x1bab5, 0x1bad4, 0x1bad7, 0x1badc, 0x1bae3, 0x1bb0e, 0x1bb25, 0x1bb2b, 0x1bb33, 0x1bb44, 0x1bb47, 0x1bb4a, 0x1bb4b, 0x1bb89, 0x1bba7, 0x1bbbc, 0x1bbbd, 0x1bbca, 0x1bbf0, 0x1bbf0, 0x1bbf6, 0x1bbf6, 0x1bbf6, 0x1bc29, 0x1bc73, 0x1bc88, 0x1bc94, 0x1bd76, 0x1bd7d, 0x1bda8, 0x1bdca, 0x1beb3, 0x1bec0, 0x1bec0, 0x1bec1, 0x1bec1, 0x1bec1, 0x1bec7, 0x1bee1, 0x1bee4, 0x1beea, 0x1beec, 0x1c06e, 0x1c071, 0x1c07e, 0x1c080, 0x1c089, 0x1c08e, 0x1c090, 0x1c120, 0x1c12f, 0x1c134, 0x1c36c, 0x1c36e, 0x1c36f, 0x1c385, 0x1c387, 0x1c389, 0x1c38a, 0x1c38c, 0x1c38c, 0x1c399, 0x1c39c, 0x1c39e, 0x1c3be, 0x1cf51, 0x1cf6d, 0x1cfbc, 0x1d0c3, 0x1d124, 0x1d139, 0x1d142, 0x1d1d3, 0x1d1d9, 0x1d1de, 0x1d1ed, 0x1d1f5, 0x1d209, 0x1d269, 0x1d274, 0x1d27b, 0x1d2c4, 0x1d2c5, 0x1d2c9, 0x1d405, 0x1d517, 0x1d5cf, 0x1d60a, 0x1d61f, 0x1d640, 0x1d646, 0x1d663, 0x1d667, 0x1d667, 0x1d689, 0x1d6b5, 0x1d6b9, 0x1d6ba, 0x1d6ba, 0x1d6ba, 0x1d70d, 0x1d719, 0x1d766, 0x1d784, 0x1d78e, 0x1d79a, 0x1d7df, 0x1d8da, 0x1d8df, 0x1d8e5, 0x1d8ee, 0x1d95a, 0x1d963, 0x1d96c, 0x1d97f, 0x1d9b6, 0x1d9b8, 0x1d9b8, 0x1d9c1, 0x1d9cb, 0x1d9de, 0x1db1e, 0x1db1e, 0x1db1e, 0x1db27, 0x1db29, 0x1db2c, 0x1db2e, 0x1db2e, 0x1db2e, 0x1db2e, 0x1db30, 0x1db5a, 0x1db5c, 0x1db73, 0x1db7a, 0x1db7a, 0x1db7e, 0x1db9d, 0x1db9f, 0x1dbc0, 0x1dc3e, 0x1dc40, 0x1e759, 0x1e761, 0x1e761, 0x1e761, 0x1e761, 0x1e7b5, 0x1e7ca, 0x1e7d0, 0x1e7d3, 0x1e7d9, 0x1e7dd, 0x1e802, 0x1e805, 0x1e809, 0x1ec2b, 0x1eda9, 0x1edbf, 0x1ee68, 0x1ee77, 0x1ee90, 0x1eefe, 0x1f164, 0x1f16d, 0x1f17e, 0x1f17e, 0x1f18c, 0x1f1b0, 0x1f21c, 0x1f229, 0x1f365, 0x1f374, 0x1f377, 0x1f3b0, 0x1f3b2, 0x1f3b2, 0x1f3b4, 0x1f3b6, 0x1f3bd, 0x1f428, 0x1f56e, 0x1f5c0, 0x1f6c2, 0x1f6c4, 0x1f6d5, 0x1f6d5, 0x1f6e3, 0x1f712, 0x1f9e8, 0x203d8, 0x2048f, 0x20516, 0x20561, 0x20801, 0x20a35, 0x20a37, 0x20a39, 0x20a3a, 0x20a3a, 0x20a3c, 0x20bac, 0x20c0e, 0x20c10, 0x20c19, 0x20c4f, 0x20d4e, 0x21185, 0x211e5, 0x21ca3, 0x21caa, 0x21d32, 0x21e0a, 0x22035, 0x2214c, 0x22273, 0x2249a, 0x22852, 0x22936, 0x2296e, 0x22977, 0x22981, 0x22a0c, 0x22a0f, 0x22a13, 0x22aed, 0x22c00, 0x23687, 0x23ce7, 0x23d6c, 0x23e2b, 0x23ee4, 0x2401e, 0x243cd, 0x243d7, 0x243df, 0x243ec, 0x243f2, 0x24427, 0x2442d, 0x24431, 0x24438, 0x2443c, 0x24442, 0x24445, 0x24474, 0x2447e, 0x244bd, 0x244d7, 0x24533, 0x24534, 0x24546, 0x24575, 0x24584, 0x2458c, 0x24592, 0x245ac, 0x24738, 0x254ee, 0x25516, 0x2551f, 0x25523, 0x2552c, 0x2552f, 0x2553e, 0x274f7, 0x27c23, 0x27c71, 0x27c7f, 0x27c82, 0x27cba, 0x27d25, 0x28d31, 0x2942f, 0x2943d, 0x29440, 0x29466, 0x29471, 0x29490, 0x29496, 0x2949e, 0x294b1, 0x29737, 0x2ca35, 0x2ca7d, 0x2ca87, 0x2ca88, 0x2ca89, 0x2ca8f, 0x2ca9a, 0x2d56c, 0x2d715, 0x2dcd6, 0x2dd6f, 0x2fd71, 0x30024, 0x3011a, 0x30839, 0x30a56, 0x30a65, 0x30a6b, 0x30a6f, 0x30a95, 0x30a9d, 0x30aa1, 0x30adb, 0x30af4, 0x30e9d, 0x30eea, 0x30eed, 0x30eee, 0x30eee, 0x30eee, 0x30eee, 0x30eff, 0x3107e, 0x31081, 0x31085, 0x31085, 0x31086, 0x31086, 0x31086, 0x31086, 0x31086, 0x31086, 0x31086, 0x31086, 0x31086, 0x31086, 0x31086, 0x31086, 0x31086, 0x3108c, 0x3108e, 0x31093, 0x31096, 0x31096, 0x31096, 0x31096, 0x31096, 0x3109d, 0x3109e, 0x3109e, 0x310ae, 0x310c2, 0x310c2, 0x310c2, 0x310c2, 0x310c2, 0x310c2, 0x310c2, 0x310c2, 0x31147, 0x311aa, 0x311aa, 0x311aa, 0x311aa, 0x311aa, 0x311c5, 0x311cc, 0x313f6, 0x314a1, 0x31530, 0x31531, 0x315ec, 0x31608, 0x3160a, 0x31716, 0x31859, 0x318be, 0x3192e ]

all_inputs = []

for block in blocks:
    block = web3.eth.get_block(block)
    # print(len(block.transactions))

    for tx_hash in block.transactions:
        # Get the transaction object from the hash
        tx = web3.eth.get_transaction(tx_hash)['input']
        print(int(Web3.soliditySha3(['uint256', 'uint256', 'uint256'], [1 ,2, 3]), 16))

        all_inputs.append(tx)


freq_map = {}
for key in all_inputs:
    if key in freq_map:
        freq_map[key] += 1
    else:
        freq_map[key] = 1


sorted_freq = dict(sorted(freq_map.items(), key=lambda x: x[1], reverse=True))

print(sorted_freq)

'''

uint256 hash = uint256(keccak256(abi.encode(nonce)));


all_inputs = [0x3ac44d41, 0x53582876]
f = open("all_inputs.txt", "r")
# lines = f.readlines()
for line in all_inputs:
    tx = line
    # tx = int(line, 16)

    try:
        nonce_encoded = encode_abi(['uint256'], [tx])
        

        # Calculate the keccak256 hash of the encoded nonce
        keccak_hash = web3.keccak(nonce_encoded)

        # Convert the keccak256 hash to a uint256 value
        uint256_hash = int.from_bytes(keccak_hash, byteorder='big')

        # Print the uint256 hash value
        print(hex(uint256_hash))

    except:
        print('error for '+ str(tx))
        break


'''




'''
for block_number in blocks:
    block = web3.eth.get_block(block_number)
    # print(len(block.transactions))

    for tx_hash in block.transactions:
        # Get the transaction object from the hash
        tx = web3.eth.get_transaction(tx_hash)['input']
        all_inputs.append(tx)


unique_inputs = list(set(all_inputs))


for ele in unique_inputs:
    f.write(ele + "\n")




        # if tx == '0x':
        #     continue
        # else:
        #     try:
        #         nonce_encoded = encode_abi(['uint256'], [int(tx)])

        #         # Calculate the keccak256 hash of the encoded nonce
        #         keccak_hash = web3.keccak(nonce_encoded)

        #         # Convert the keccak256 hash to a uint256 value
        #         uint256_hash = int.from_bytes(keccak_hash, byteorder='big')

        #         # Print the uint256 hash value
        #         print(hex(uint256_hash))
        #     except:
        #         print('Error for tx '+ tx)
        
        # print(tx)




# for i in range(total_tx):
#     # Get the hash of the i-th transaction from the address
#     # tx_hash = web3.eth.get_transaction_by_index(address, i)
    

#     tx_hash = web3.eth.getTransactionByBlock() # transactions.get(i, block_identifier=None)

#     # Get the transaction object from the hash
#     tx = web3.eth.get_transaction(tx_hash)

#     # Print the transaction object
#     print(tx)
'''

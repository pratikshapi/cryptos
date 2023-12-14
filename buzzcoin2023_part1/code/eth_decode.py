import eth_abi

# Decode the input data using the function signature and parameter types
function_signature = 'problem5(uint)'
parameter_types = ['uint']
input_data = '0x35ea8270'
bytes.fromhex(input_data[2:])
decoded_data = eth_abi.decode_abi(parameter_types, bytes.fromhex(input_data[2:]))

# Process the decoded data as needed
myArg1 = decoded_data
print(myArg1)
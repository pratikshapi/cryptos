import json
from collections import defaultdict


# Open the input file
with open('blocks.json', 'r') as f:
    data = json.load(f)

output_dict = defaultdict(list)

# some_address = "0x1421350ab6660421d2EA4e423a52030c9A19010E".lower()

with open('address_greater_than_100', 'r') as input_file:
    f = input_file.readlines()
    for line in f:
        # print(line)
        line_address = line.strip('\n').lower()
        print(line_address)
        for element in data:
            # Extract the "from" and "to" values from the element
            from_val = element['from']
            to_val = element['to']
            # print(from_val, to_val)
            if from_val == line_address or to_val == line_address:
                output_dict[line_address].append(element['input'])
    

# Open the output file and write the output dictionary as a JSON object
with open('output.json', 'w') as out:
    json.dump(output_dict, out)

with open('output.txt', 'w') as out:
    json.dump([v for k, v in output_dict.items()], out)
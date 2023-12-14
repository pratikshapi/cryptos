# Open input file and read comma-separated values into a list
with open('output_unique.txt', 'r') as f:
    csv_data = f.read().splitlines()

# Create an empty list to store the extracted values
values = []

# Iterate through the CSV data and extract the values
for line in csv_data:
    values.extend(line.split('\n'))

# Find unique values
# unique_values = set(values)

with open('output_unique_integers.txt', 'w') as  f:
    for value in values:
        try:
            f.write(int(value) + ',')
        except Exception as e:
            print('Unable to write for value', value)


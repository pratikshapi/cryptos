# Open input and output files
with open('allInputsUnique', 'r') as infile, open('allInputsUniqueInt', 'w') as outfile:
    # Loop through each line in the input file
    for line in infile:
        # Strip whitespace from the beginning and end of the line
        line = line.strip()

        # Convert the line from hex to int
        int_value = int(line, 16)
        print(int_value)

        # Write the integer value to the output file
        outfile.write(str(int_value) + '\n')
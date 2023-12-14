# Open input and output files
with open('allInputs', 'r') as infile, open('allInputsUnique', 'w') as outfile:
    # Create a set to store unique lines
    unique_lines = set()
    
    # Loop through each line in the input file
    for line in infile:
        # Strip whitespace from the beginning and end of the line
        line = line.strip()
        
        # Add the line to the set if it's not already there
        if line not in unique_lines:
            unique_lines.add(line)
            # Write the unique line to the output file
            outfile.write(line + '\n')
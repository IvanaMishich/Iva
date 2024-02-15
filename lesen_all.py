import re

def extract_values_from_lines(line):
    # Use regular expressions to extract the values of X, Y, and Z
    match = re.findall(r"KN  NAME[=][']\w+['] X[=]([-]?\d+[.]\d+) Y[=]([-]?\d+[.]?\d+) Z[=]([-]?\d+[.]?\d+)", line)
    x, y, z = (), (), ()
    if match != None:
    	for c in match:
    	    x = x+(c[0],)
    	    y = y+(c[1],)
    	    z = z+(c[2],)
    	return x, y, z

    return None

def save_values_to_file(x, y, z, output_filename):
    with open(output_filename, 'w') as output_file:
        output_file.write(f"X: {x}\nY: {y}\nZ: {z}\n")

# File names
input_filename = "input.txt"
output_filename = "output.txt"

try:
    # Open the input file and read the line
    with open(input_filename, 'r') as input_file:
        input_line = input_file.read()

        # Extract the values of X, Y, and Z
        values = extract_values_from_lines(input_line)

        if values is not None:
            x, y, z = values

            # Save the values to the output file
            save_values_to_file(x, y, z, output_filename)
            print(f"The values have been successfully saved to '{output_filename}'.")
        else:
            print("The values of X, Y, and Z could not be extracted.")
except FileNotFoundError:
    print(f"The input file '{input_filename}' was not found.")
except Exception as ex:
    print(f"An error occurred: {ex}")
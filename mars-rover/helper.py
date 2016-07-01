# Helper function to ensure instructions are the correct format
def validate_instructions(instructions):
	if instructions.isalpha() and not instructions.upper().replace("L", "").replace("R", "").replace("M", ""):
		return True
	else:
		raise ValueError("Invalid instruction input. Combinations of 'L', 'R' & 'M' are only allowed.")

# Check the plateau iinput
def validate_plateau_coordinates(coor):
	coor = input_converter(coor)
	c = [int(i) for i in coor if i.isdigit()]
	if c and len(c) == 2:
		return coor
	else:
		raise ValueError("Invalid coordinate entry. Only 2 <int> entries allowed.")

# Validates rover input. 
# Input should be: <int> <int> <coordinate>, i.e, 1 2 N
def validate_rover_input(x, y, dir):
	if x.isdigit() and y.isdigit() and dir.upper() in ["N", "W", "S", "E"] and len(dir) == 1:
		return [x, y, dir]
	else:
		raise ValueError("Invalid Rover input. Input should be: <int> <int> <coordinate>")		

# Converts string into dictionary for easy function calling
def input_converter(input, max_value=2):
	input = input_to_list(input)[:max_value]
	if len(input) == max_value:
		print "> First %s input values used: %s" % (max_value, input)
		return input
	else:
		raise ValueError("Invalid input. Number of entries is not the expected one. Expected: %s" % max_value)

# Converts input string to list
def input_to_list(input):
	return input.strip().split()

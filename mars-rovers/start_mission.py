import sys
import rover as r
import helper

class Plateau(object):
	# Variable that can easily be changes to increment total number of Rovers
	NUMBER_OF_ROVERS = 2

	# Chose to associate 2 Rover with a Plateau object.
	# This way, the plateau and all corresponding Rovers are
	# initialized together.
	# This setup also allows more Rovers to be added with major changes.
	def __init__(self, x, y, test=False):
		self.x = x
		self.y = y
		# More Rovers can be added very easily
		if not test:
			self.rovers = [self.new_rover(i + 1) for i in range(self.NUMBER_OF_ROVERS)]

	def __repr__(self):
		return "<Plateau X:%s Y:%s>" % (self.x, self.y)

	def new_rover(self, index):
		rover_input = raw_input(">> Enter Rover#%s information: " % index)
		try:
			rover_input = helper.input_converter(rover_input, 3)
			validated_input = helper.validate_rover_input(*rover_input)
			if validated_input:
				return self.initialize_rover(*validated_input + [index])
		except ValueError as e:
			print e.message
			sys.exit(1)
		

	# Creatives a new Rober object based on user"s input
	def initialize_rover(self, x, y, dire, index):
		rover_data = dict(
			x=x,
			y=y,
			direction=dire)
		rover = r.Rover(**rover_data)
		print "> Rover#%s created!" % index
		commands = raw_input(">> Enter instructions for Rover#%s: " % index)
		if helper.validate_instructions(commands.upper()):
			for c in commands:
				rover.execute(c.upper())
			return rover

# This function starts by creating a Plateau and then
# all dependent Rover objects are created based on the user input.
def start_mission():
	coordinates = raw_input(">> Enter plateau upper-right coordinates:")
	try:
		p = helper.validate_plateau_coordinates(coordinates)
		if p:
			plateau = Plateau(*p)
			print "> OUTPUT:"
			for rover in plateau.rovers:
				print rover.get_location()
	except ValueError as e:
		print e.message
		sys.exit(1)

if __name__ == "__main__":
	start_mission()

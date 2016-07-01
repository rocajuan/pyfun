class Rover(object):
	# Predefined step size for movement.
	# This variable will allow for future increase in grid size.
	STEP_SIZE = 1

	# Direction variables--
	##  For readability purposes.
	RIGHT = "R"
	LEFT = "L"
	NORTH = "N"
	SOUTH = "S"
	WEST = "W"
	EAST = "E"

	# Directions mappings--
	# It denotes the possible turning combinations
	# based on current direction the Rover is facing.
	## Again readability.
	COMPASS = {
		NORTH: {RIGHT: EAST, LEFT: WEST},
		SOUTH: {RIGHT: WEST, LEFT: EAST},
		EAST: {RIGHT: SOUTH, LEFT: NORTH},
		WEST: {RIGHT: NORTH, LEFT: SOUTH}
	}

	def __init__(self, x, y, direction):
		self.direction = direction.upper()
		self.x = int(x)
		self.y = int(y)
		self.location = "%s %s %s" % (self.x, self.y, self.direction)

	def __repr__(self):
		return "<Rover X:%s Y:%s Direction:%s>" % (self.x, self.y, self.direction)

	# Rover moves depending on the current direction it is facing
	def move(self):
		_dir = self.direction
		if _dir == self.NORTH:
			self.y += self.STEP_SIZE
		elif _dir == self.SOUTH:
			self.y -= self.STEP_SIZE
		elif _dir == self.WEST:
			self.x -= self.STEP_SIZE
		else:
			self.x += self.STEP_SIZE
		self.refresh_location()
		#print "Moved %s by %s step" % (_dir, self.STEP_SIZE) #DEBUG

	# Rover turns to specific direction & updates current location
	def turn(self, turn):
		self.direction = self.COMPASS[self.direction][turn]
		self.refresh_location()
		#print "Turned %s." % turn.upper() #DEBUG

	# Refresh the location variable with the updated X,Y coordinates
	def refresh_location(self):
		self.location = "%s %s %s" % (self.x, self.y, self.direction)

	# Returns Rover's location
	def get_location(self):
		return self.location

	# Function to parse every command and decide what the Rover should do
	def execute(self, action):
		if action in ["L", "R"]:
			self.turn(action)
		elif action == "M":
			self.move()
		else:
			raise ValueError("Invalid action.")

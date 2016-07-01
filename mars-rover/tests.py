import unittest
import rover as r
import start_mission as s
import helper as h

class MissionTest(unittest.TestCase):
	x_test = "1"
	y_test = "1"
	dir_test = "E"
	test_enabled = True

	## Rover
	# Ensure the creation process is correct
	def test_rover_creation(self):
		rover = r.Rover(self.x_test, self.y_test, self.dir_test)
		self.assertEqual(rover.x, int(self.x_test))
		self.assertEqual(rover.y, int(self.y_test))
		self.assertEqual(rover.direction, self.dir_test)

	# Test Rover input values
	def test_rover_invalid_x_parameter(self):
		self.assertRaises(ValueError, r.Rover, "a", "1", "N")

	def test_rover_invalid_y_parameter(self):
		self.assertRaises(ValueError, r.Rover, "2", "b", "N")

	def test_rover_invalid_direction_parameter(self):
		self.assertRaises(ValueError, r.Rover, "2", "b", "1")
		
	def test_rover_inputs(self):
		rover = r.Rover("2", "2", "N")
		d = rover.direction
		self.assertTrue(str(rover.x).isdigit())
		self.assertFalse(str(rover.x).isalpha())
		self.assertTrue(str(rover.y).isdigit())
		self.assertFalse(str(rover.y).isalpha())
		self.assertTrue(d.isalpha() and d in ["N", "S", "E", "W"] and len(d) ==1)
		self.assertFalse(rover.direction.isdigit())

	# Tests rover movement
	def test_rover_movement_north(self):
		rover = r.Rover(self.x_test, self.y_test, "N")
		rover.move()
		self.assertEqual(rover.y, int(self.y_test) + rover.STEP_SIZE)

	def test_rover_movement_south(self):
		rover = r.Rover(self.x_test, self.y_test, "S")
		rover.move()
		self.assertEqual(rover.y, int(self.y_test) - rover.STEP_SIZE)

	def test_rover_movement_east(self):
		rover = r.Rover(self.x_test, self.y_test, "E")
		rover.move()
		self.assertEqual(rover.x, int(self.x_test) + rover.STEP_SIZE)

	def test_rover_movement_west(self):
		rover = r.Rover(self.x_test, self.y_test, "W")
		rover.move()
		self.assertEqual(rover.x, int(self.x_test) - rover.STEP_SIZE)

	# Test invalid command
	def test_rover_execute_with_invalid_command(self):
		rover = r.Rover(self.x_test, self.y_test, "W")
		self.assertRaises(ValueError, rover.execute, "X")

	# Tests turning logic for all directions
	def test_rover_turn_right_when_facing_north(self):
		rover = r.Rover(self.x_test, self.y_test, "N")
		rover.turn("R")
		self.assertEqual(rover.direction, "E")

	def test_rover_turn_right_when_facing_east(self):
		rover = r.Rover(self.x_test, self.y_test, "E")
		rover.turn("R")
		self.assertEqual(rover.direction, "S")

	def test_rover_turn_right_when_facing_south(self):
		rover = r.Rover(self.x_test, self.y_test, "S")
		rover.turn("R")
		self.assertEqual(rover.direction, "W")

	def test_rover_turn_right_when_facing_west(self):
		rover = r.Rover(self.x_test, self.y_test, "W")
		rover.turn("R")
		self.assertEqual(rover.direction, "N")

	def test_rover_turn_left_when_facing_north(self):
		rover = r.Rover(self.x_test, self.y_test, "N")
		rover.turn("L")
		self.assertEqual(rover.direction, "W")

	def test_rover_turn_left_when_facing_east(self):
		rover = r.Rover(self.x_test, self.y_test, "E")
		rover.turn("L")
		self.assertEqual(rover.direction, "N")

	def test_rover_turn_left_when_facing_south(self):
		rover = r.Rover(self.x_test, self.y_test, "S")
		rover.turn("L")
		self.assertEqual(rover.direction, "E")

	def test_rover_turn_left_when_facing_west(self):
		rover = r.Rover(self.x_test, self.y_test, "W")
		rover.turn("L")
		self.assertEqual(rover.direction, "S")

	# Tests the Rover"s location function
	def test_rover_get_location(self):
		rover = r.Rover(self.x_test, self.y_test, self.dir_test)
		self.assertTrue("%s %s %s" % (self.x_test, self.y_test, self.dir_test) == rover.get_location())

	## Plateau testcases
	# Test plateau coordinates
	def test_plateau_coordinates_numbers(self):
		plateau = s.Plateau(self.x_test, self.y_test, self.test_enabled)
		self.assertTrue(plateau.x.isdigit())
		self.assertTrue(plateau.y.isdigit())

	## test.py
	# Test instruction input & behaviour
	def test_integer_instructions(self):
		self.assertRaises(ValueError, h.validate_instructions, "2")

	def test_invalid_instructions(self):
		self.assertRaises(ValueError, h.validate_instructions, "W")

	def test_empty_instructions(self):
		self.assertRaises(ValueError, h.validate_instructions, "")

	# Test coordinate check
	def test_non_digit_coordinates(self):
		self.assertRaises(ValueError, h.validate_plateau_coordinates, "TEST 1")

	def test_too_few_coordinates(self):
		self.assertRaises(ValueError, h.validate_instructions, "1")

	def test_empty_coordinates(self):
		self.assertRaises(ValueError, h.validate_instructions, "")


if __name__ == "__main__":
	unittest.main()

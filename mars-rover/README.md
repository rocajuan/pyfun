# Rover assignment description

A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously
rectangular, must be navigated by the rovers so that their onboard cameras can get a complete view of the
surrounding terrain to send back to Earth.

A rover's position and location is represented by a combination of X and X coordinates and a letter
representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify
navigation. An example position might be (0, 0, N), which means the rover is in the bottom
left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L'
and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot. 'M'
means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

INPUT:
The first line of input is the upperright coordinates of the plateau, the lowerleft coordinates are assumed to
be 0,0.
The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two
lines of input. The first line gives the rover's position, and the second line is a series of instructions telling
the rover how to explore the plateau.
The position is made up of two integers and a letter separated by spaces, corresponding to the X and Y
coordinates and the rover's orientation.

Each rover will be finished sequentially, which means that the second rover won't start to move until the first
one has finished moving.

OUTPUT
The output for each rover should be its final coordinates
and heading.

# Test Input
5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM

# Expected Output:
1 3 N
5 1 E

# Solution
Here is the breakdown of the files included:

`rover.py` -- Rover object file including all functions and variables belonging to the Rover object.

`start_mission.py` -- This file includes the main function and has a definition of the Plateau object which is currently set to contain 2 Rover objects and the plateau coordinates.

`helper.py` -- Helper scripts containing minor functions needed for input parsing and other small functions.

`tests.py` -- File containing all the tests wrote for these classes and functions.


# Setup/Usage
To run the application, simply go the directory storing the files and run:
`python start_mission.py`

Certain prompts will ask the user for the information/input needed to run the program.

# Testing
To run this tests, just run:
`python tests.py` 

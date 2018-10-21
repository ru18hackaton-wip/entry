import py_trees
from .behaviors.movement import Move, MoveUntilNewBiome
from .behaviors.distance import CloseEnough
from .behaviors.light import Color, ScanFloor
from .behaviors.follow_line import FollowLine

# Create the behavior tree for intro part

def create_intro_tree(robot):
    root = py_trees.composites.Sequence(name="Intro")
    scan = ScanFloor()
    scan.setup(0, robot=robot)
    scanner = py_trees.idioms.oneshot("Floor data", "floor_scanned", scan)
    move = MoveUntilNewBiome()
    move.setup(0, robot=robot, speeds=[100,100])
    root.add_children([scanner, move])
    return py_trees.idioms.oneshot("The Intro", "intro", root)

# Ramppi
# Suoraan -> Vasen 90 astetta
# Suoraan -> Vasen 90 astetta
# Suoraan -> Oikea 90 astetta
# Suoraan -> Oikea 90 astetta
# Suoraan -> Oikea 45 astetta
# Suoraan -> Oikea 45 astetta
# Suoraan -> Ei vasen 0 astetta
# Suoraan -> Keltainen 180 astetta
# Suoraan -> Oikea 90 astetta
# Suoraan -> Vasen 90 astetta
# Suoraan -> Oikea 90 astetta
# Suoraan -> Ei vasen 0 astetta
# Suoraan -> Oikea 90 astetta
# Suoraan -> Vasen 90 astetta
# Ramppi
def _create_follow_line_tree(robot):
    root = py_trees.composites.Selector("Follow line")
    always_left = Move("I see white, turn right")
    always_left.setup(15, robot, [30, 5])
    too_much_right = FollowLine("I see black, turn left")
    too_much_right.setup(15, robot, "Black", [5,30])
    root.add_children([too_much_right, always_left])
    return root

# Create the behavior tree for the maze

def create_maze_tree(robot):
    maze = _create_follow_line_tree(robot)
    mazec = py_trees.idioms.oneshot("Maze", "maze", maze)
    return mazec

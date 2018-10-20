import py_trees
from .behaviors.movement import Move
from .behaviors.distance import CloseEnough
from .behaviors.light import Color
from .behaviors.follow_line import FollowLine

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

def create_track01_tree(robot):
    return _create_follow_line_tree(robot)

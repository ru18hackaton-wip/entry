import py_trees
from .behaviors.movement import Forward, TurnLeft
from .behaviors.distance import CloseEnough

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
def create_track01_tree(robot):
    return None

def create_crash_avoider_tree(robot):
    root = py_trees.composites.Selector("root")
    avoid = py_trees.composites.Parallel("Avoid obstacle")
    too_close = CloseEnough()
    too_close.setup(15, robot, 20)
    forward = Forward()
    forward.setup(15, robot)
    turn = TurnLeft()
    turn.setup(15, robot)
    avoid.add_children([too_close, turn])
    root.add_children([avoid, forward])
    return root

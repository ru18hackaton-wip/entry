import py_trees
from .behaviors.movement import Move
from .behaviors.distance import CloseEnough
from .behaviors.light import Color

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
def _create_follow_tape_adjust_left_tree(robot):
    adjust = py_trees.composites.Parallel("Adjust left", py_trees.common.ParallelPolicy.SUCCESS_ON_ALL)
    turn = Move()
    turn.setup(15, robot, 80, 100)
    see_tape = Color()
    see_tape.setup(15, robot, "Black")
    adjust.add_children([see_tape, turn])
    return adjust

def _create_follow_tape_adjust_right_tree(robot):
    adjust = py_trees.composites.Parallel("Adjust right", py_trees.common.ParallelPolicy.SUCCESS_ON_ALL)
    turn = Move()
    turn.setup(15, robot, 100, 80)
    see_tape = Color()
    see_tape.setup(15, robot, "White")
    adjust.add_children([see_tape, turn])
    return adjust

def create_track01_tree(robot):
    root = py_trees.composites.Selector("root")
    adjust_left = _create_follow_tape_adjust_left_tree(robot)
    adjust_right = _create_follow_tape_adjust_right_tree(robot)
    root.add_children([adjust_left, adjust_right])
    return root

def create_crash_avoider_tree(robot):
    root = py_trees.composites.Selector("root")
    avoid = py_trees.composites.Parallel("Avoid obstacle")
    too_close = CloseEnough()
    too_close.setup(15, robot, 20)
    forward = Move()
    forward.setup(15, robot, 100, 100)
    turn = Move()
    turn.setup(15, robot, 0, 100)
    avoid.add_children([too_close, turn])
    root.add_children([avoid, forward])
    return root

from .robot import Robot
from .runner import Runner
from .behaviors.movement import Forward, TurnLeft
from .behaviors.distance import CloseEnough

import py_trees

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
    tree = py_trees.trees.BehaviourTree(root)
    tree.setup(timeout=15)
    return tree

def main():
    robot = Robot()
    runner = Runner(robot)

    tree = create_crash_avoider_tree(robot)
    runner.set_tree(tree)

    runner.run()

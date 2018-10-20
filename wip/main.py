from .robot import Robot
from .runner import Runner
from .behaviors.forward import Forward
from .behaviors.distance import CloseEnough

import py_trees

def create_crash_avoider_tree(robot):
    root = py_trees.composites.Selector("root")
    too_close = CloseEnough()
    too_close.setup(15, robot, 20)
    forward = Forward()
    forward.setup(15, robot)
    root.add_children([too_close, forward])
    tree = py_trees.trees.BehaviourTree(root)
    tree.setup(timeout=15)
    return tree

def main():
    robot = Robot()
    runner = Runner(robot)

    tree = create_crash_avoider_tree(robot)
    runner.set_tree(tree)

    runner.run()

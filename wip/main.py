from .robot import Robot
from .runner import Runner

import py_trees

def create_tree():
    root = py_trees.composites.Selector("root")
    success_after_two = py_trees.behaviours.Count(name="After Two",
                                                  fail_until=2,
                                                  running_until=2,
                                                  success_until=4)
    always_running = py_trees.behaviours.Running(name="Running")
    root.add_children([success_after_two, always_running])
    tree = py_trees.trees.BehaviourTree(root)
    tree.setup(timeout=15)
    return tree

def main():
    robot = Robot()
    runner = Runner(robot)


    tree = create_tree()
    runner.set_tree(tree)

    runner.run()

from .robot import Robot
from .runner import Runner
from .behaviors.forward import Forward

import py_trees

def create_tree(robot):
    root = py_trees.composites.Selector("root")
    success_after_two = py_trees.behaviours.Count(name="After Two",
                                                  fail_until=2,
                                                  running_until=2,
                                                  success_until=4)
    always_running = Forward()
    always_running.setup(15, robot)
    root.add_children([success_after_two, always_running])
    tree = py_trees.trees.BehaviourTree(root)
    tree.setup(timeout=15)
    return tree

def main():
    robot = Robot()
    runner = Runner(robot)


    tree = create_tree(robot)
    runner.set_tree(tree)

    runner.run()

from .robot import Robot
from .runner import Runner

from .tracks import create_crash_avoider_tree

def main():
    robot = Robot()
    runner = Runner(robot)

    tree = create_crash_avoider_tree(robot)
    runner.set_tree(tree)

    runner.run()

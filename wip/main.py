from .robot import Robot
from .runner import Runner

from .tracks import create_track01_tree

def main():
    robot = Robot()
    runner = Runner(robot)

    tree = create_track01_tree(robot)
    runner.set_tree(tree)

    runner.run()

if __name__ == "__main__":
    main()

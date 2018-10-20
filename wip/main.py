from .robot import Robot
from .runner import Runner
from .www import Webserver
from ev3dev2.control.webserver import WebControlledTank

from .tracks import create_track01_tree

def main():
    robot = Robot()
    runner = Runner(robot)
    www = WebControlledTank()

    tree = create_track01_tree(robot)
    runner.set_tree(tree)

    runner.run()
    www.main()

if __name__ == "__main__":
    main()

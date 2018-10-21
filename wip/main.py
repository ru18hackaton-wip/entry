from .robot import Robot
from .runner import Runner

from .tracks import create_intro_tree, create_track01_tree
from .behaviors.greetings import Welcome

import py_trees

def _create_welcome_section(robot):
    welcome = Welcome()
    welcome.setup(0,robot)
    wconce = py_trees.idioms.oneshot("Welcome once", "welcome", welcome)
    return wconce

def main():
    robot = Robot()
    runner = Runner(robot)

    root = py_trees.composites.Sequence(name="root")
    welcome = _create_welcome_section(robot)
    intro = create_intro_tree(robot)
    tracks = py_trees.composites.Sequence(name="Tracks")
    track1 = create_track01_tree(robot)
    tracks.add_children([track1])
    root.add_children([welcome, intro, tracks])
    runner.set_tree(root)

    runner.run()

if __name__ == "__main__":
    main()

from .robot import Robot
from .runner import Runner

from .tracks import create_intro_tree, create_track01_tree
from .behaviors.greetings import Welcome
from .behaviors.biome import Analyzer

from .helpers import Biome

import py_trees

def init():
    bb = py_trees.blackboard.Blackboard()
    bb.set("biome_check", False)
    bb.set("biome_type", Biome.FLOOR)

def _create_welcome_section(robot):
    welcome = Welcome()
    welcome.setup(0,robot)
    wconce = py_trees.idioms.oneshot("Welcome once", "welcome", welcome)
    return wconce

def _create_tools_tree(robot):
    analyzer = Analyzer()
    analyzer.setup(0, robot)

    tools = py_trees.composites.Selector(name="Tools")
    tools.add_children([analyzer])
    return tools

def main():
    init()
    robot = Robot()
    runner = Runner(robot)

    root = py_trees.composites.Selector(name="Main tree")
    tools = _create_tools_tree(robot)

    behaviors = py_trees.composites.Sequence(name="WIP AI behaviors")
    welcome = _create_welcome_section(robot)
    intro = create_intro_tree(robot)
    tracks = py_trees.composites.Sequence(name="Tracks")
    track1 = create_track01_tree(robot)
    tracks.add_children([track1])
    behaviors.add_children([welcome, intro, tracks])

    root.add_children([tools, behaviors])
    runner.set_tree(root)

    runner.run()

if __name__ == "__main__":
    main()

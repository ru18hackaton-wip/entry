from .robot import Robot
from .runner import Runner

from .tracks import create_intro_tree, create_maze_tree
from .behaviors.greetings import Welcome
from .behaviors.biome import Analyzer

from .helpers import Biome

import py_trees

# Initializes robot

def init():
    bb = py_trees.blackboard.Blackboard()
    bb.set("biome_check", False)
    bb.set("biome_type", Biome.FLOOR)

# Creates welcome section

def _create_welcome_section(robot):
    welcome = Welcome()
    welcome.setup(0,robot)
    wconce = py_trees.idioms.oneshot("Welcome once", "welcome", welcome)
    return wconce

# Creates the tools tree

def _create_tools_tree(robot):
    analyzer = Analyzer()
    analyzer.setup(0, robot)

    tools = py_trees.composites.Selector(name="Tools")
    tools.add_children([analyzer])
    return tools

# Main program initializes the behavior trees for the entire
# program

def main():
    init()
    robot = Robot()
    runner = Runner(robot)

    tools = _create_tools_tree(robot)

    behaviors = py_trees.composites.Selector(name="WIP AI behaviors")
    welcome = _create_welcome_section(robot)
    intro = create_intro_tree(robot)
    tracks = py_trees.composites.Sequence(name="Tracks")
    maze = create_maze_tree(robot)
    tracks.add_children([welcome, intro, maze])
    behaviors.add_children([tools, tracks])

    runner.set_tree(behaviors)

    runner.run()

if __name__ == "__main__":
    main()

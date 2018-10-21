import time
import py_trees

def draw_tree(tree):
    py_trees.display.print_ascii_tree(tree.root, show_status=True)
    print(py_trees.blackboard.Blackboard())

# Class defines the control loop for the robot

class Runner:

    def __init__(self, robot):
        self.robot = robot
        self.tick_rate = 500

    # Sets the tick rate

    def set_tick_rate(self, value):
        self.tick_rate = value

    # Sets the behaviour tree for the control loop

    def set_tree(self, root):
        tree = py_trees.trees.BehaviourTree(root)
        tree.setup(timeout=15)
        self.tree = tree

    # Control loop for the robot

    def run(self):
        try:
            self.tree.tick_tock(
                sleep_ms=self.tick_rate,
                number_of_iterations=py_trees.trees.CONTINUOUS_TICK_TOCK,
                pre_tick_handler=None,
                post_tick_handler=draw_tree
            )
        except KeyboardInterrupt:
            behaviour_tree.interrupt()

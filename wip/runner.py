import time
import py_trees

def draw_tree(tree):
    py_trees.display.print_ascii_tree(tree.root, show_status=True)

class Runner:

    def __init__(self, robot):
        self.robot = robot
        self.tick_rate = 500

    def set_tick_rate(self, value):
        self.tick_rate = value

    def set_tree(self, root):
        tree = py_trees.trees.BehaviourTree(root)
        tree.setup(timeout=15)
        self.tree = tree

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

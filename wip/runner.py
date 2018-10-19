import time
import py_trees

class Runner:

    def __init__(self, robot):
        self.robot = robot

    def set_tree(self, tree):
        self.tree = tree

    def run(self):
        for i in range(1, 6):
            try:
                print("\n--------- Tick {0} ---------\n".format(i))
                self.tree.tick_once()
                print("\n")
                py_trees.display.print_ascii_tree(self.tree, show_status=True)
                time.sleep(1.0)
            except KeyboardInterrupt:
                break
        print("\n")

import py_trees
import time
from ev3dev2.led import Leds

def create_tree():
    root = py_trees.composites.Selector("root")
    success_after_two = py_trees.behaviours.Count(name="After Two",
                                                  fail_until=2,
                                                  running_until=2,
                                                  success_until=4)
    always_running = py_trees.behaviours.Running(name="Running")
    root.add_children([success_after_two, always_running])
    return root

def main():
    print("foobarbaz")

    node = py_trees.composites.Selector("Random node")
    print(str(node))

    leds = Leds()
    leds.set_color("LEFT", "GREEN")
    print("Green!")

    tree = create_tree()
    tree.setup(timeout=15)
    for i in range(1, 6):
        try:
            print("\n--------- Tick {0} ---------\n".format(i))
            tree.tick_once()
            print("\n")
            py_trees.display.print_ascii_tree(tree, show_status=True)
            time.sleep(1.0)
        except KeyboardInterrupt:
            break
    print("\n")

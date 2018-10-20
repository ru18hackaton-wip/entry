from py_trees.behaviour import Behaviour
from py_trees.common import Status

class Color(Behaviour):

    def __init__(self, name="Color"):
        super(Color, self).__init__(name)

    def setup(self, timeout, robot=None, color=None):
        if robot:
            self.robot = robot
        if color:
            self.target_color = color
        return True

    def initialise(self):
        pass

    def update(self):
        if self.target_color == self.robot.get_color().color_name:
            return Status.SUCCESS
        else:
            return Status.FAILURE

    def terminate(self, new_status):
        pass

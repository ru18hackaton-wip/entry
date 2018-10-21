from py_trees.behaviour import Behaviour
from py_trees.common import Status

from ..helpers import same_biome

# Class defines the Behaviour of following a line

class FollowLine(Behaviour):

    def __init__(self, name="FollowLine"):
        super(FollowLine, self).__init__(name)

    # Initializes the class

    def setup(self, timeout, robot=None, color=None, speeds=None):
        if robot:
            self.robot = robot
        if color:
            self.target_color = color
        if speeds:
            self.target_speeds = speeds
        return True

    def initialise(self):
        pass

    def update(self):
        if same_biome(self.target_color, self.robot.get_color()):
            left, right = self.target_speeds
            self.robot.move(left,right)
            return Status.RUNNING
        return Status.FAILURE

    def terminate(self, new_status):
        pass

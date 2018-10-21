from py_trees.behaviour import Behaviour
from py_trees.common import Status

# Behavior node that tells if something is close enough the robot

class CloseEnough(Behaviour):

    def __init__(self, name="CloseEnough"):
        super(CloseEnough, self).__init__(name)

    def setup(self, timeout, robot=None, wanted_distance=None):
        if robot:
            self.robot = robot
        if wanted_distance:
            self.wanted_distance = wanted_distance
        return True

    def initialise(self):
        pass

    def update(self):
        distance = self.robot.get_distance()
        if distance < self.wanted_distance:
            return Status.SUCCESS
        else:
            return Status.FAILURE

    def terminate(self, new_status):
        pass

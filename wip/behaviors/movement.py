from py_trees.behaviour import Behaviour
from py_trees.common import Status

class Move(Behaviour):

    def __init__(self, name="Move"):
        super(Move, self).__init__(name)

    def setup(self, timeout, robot=None, speed_left=None, speed_right=None):
        if robot:
            self.robot = robot
        if speed_left:
            self.speed_left = speed_left
        if speed_right:
            self.speed_right = speed_right
        return True

    def initialise(self):
        pass

    def update(self):
        self.robot.move(self.speed_left,self.speed_right)
        return Status.RUNNING

    def terminate(self, new_status):
        self.robot.stop()

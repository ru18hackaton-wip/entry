from py_trees.behaviour import Behaviour
from py_trees.common import Status

class Move(Behaviour):

    def __init__(self, name="Move"):
        super(Move, self).__init__(name)

    def setup(self, timeout, robot=None, speeds=None):
        if robot:
            self.robot = robot
        if speeds:
            self.speeds = speeds
        return True

    def initialise(self):
        pass

    def update(self):
        speed_left, speed_right = self.speeds
        self.robot.move(speed_left, speed_right)
        return Status.RUNNING

    def terminate(self, new_status):
        self.robot.stop()

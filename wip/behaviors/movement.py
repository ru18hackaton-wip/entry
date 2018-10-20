from py_trees.behaviour import Behaviour
from py_trees.common import Status

class Forward(Behaviour):

    def __init__(self, name="Forward"):
        super(Forward, self).__init__(name)

    def setup(self, timeout, robot=None):
        if robot:
            self.robot = robot
        return True

    def initialise(self):
        pass

    def update(self):
        self.robot.move()
        return Status.RUNNING

    def terminate(self, new_status):
        self.robot.stop()

class TurnLeft(Behaviour):

    def __init__(self, name="TurnLeft"):
        super(TurnLeft, self).__init__(name)

    def setup(self, timeout, robot=None):
        if robot:
            self.robot = robot
        return True

    def initialise(self):
        pass

    def update(self):
        self.robot.move(0,100)
        return Status.RUNNING

    def terminate(self, new_status):
        self.robot.stop()

class TurnRight(Behaviour):

    def __init__(self, name="TurnRight"):
        super(TurnRight, self).__init__(name)

    def setup(self, timeout, robot=None):
        if robot:
            self.robot = robot
        return True

    def initialise(self):
        pass

    def update(self):
        self.robot.move(100,0)
        return Status.RUNNING

    def terminate(self, new_status):
        self.robot.stop()

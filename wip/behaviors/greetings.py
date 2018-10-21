from py_trees.behaviour import Behaviour
from py_trees.common import Status

class Welcome(Behaviour):

    def __init__(self, name="Welcome"):
        super(Welcome, self).__init__(name)

    def setup(self, timeout, robot=None):
        if robot:
            self.robot = robot
        return True

    def initialise(self):
        pass

    def update(self):
        self.robot.speak("I'm ready for Odin!")
        return Status.SUCCESS

    def terminate(self, new_status):
        pass

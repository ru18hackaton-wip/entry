from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.blackboard import Blackboard

from ..helpers import new_biome

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

class MoveUntilNewBiome(Behaviour):

    def __init__(self, name="MoveUntilNewBiome"):
        super(MoveUntilNewBiome, self).__init__(name)
        self.bb = Blackboard()

    def setup(self, timeout, robot=None, speeds=None):
        if robot:
            self.robot = robot
        if speeds:
            self.speeds = speeds
        return True

    def initialise(self):
        pass

    def update(self):
        if new_biome(self.robot.get_color(), self.bb.get("color_floor")):
            if self.status == Status.RUNNING:
                return Status.SUCCESS
        else:
            if self.status != Status.RUNNING:
                speed_left, speed_right = self.speeds
                self.robot.move(speed_left, speed_right)
                return Status.RUNNING
        return Status.FAILURE

    def terminate(self, new_status):
        if new_status == Status.SUCCESS:
            self.bb.set("biome_check", True)
            self.robot.stop()

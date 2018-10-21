from py_trees.behaviour import Behaviour
from py_trees.common import Status
from py_trees.blackboard import Blackboard

from ..helpers import analyze_type

class Analyzer(Behaviour):

    def __init__(self, name="Analyzer"):
        super(Analyzer, self).__init__(name)

    def setup(self, timeout, robot=None):
        if robot:
            self.robot = robot
        return True

    def initialise(self):
        self.turning = False
        self.color_original = None
        self.color_left = None
        self.color_right = None

    def update(self):
        bb = Blackboard()
        if bb.get("biome_check") and self.status != Status.RUNNING:
            self.color_original = self.robot.get_color()
            return Status.RUNNING
        elif self.status == Status.RUNNING:
            if not self.robot.is_running():
                if self.turning:
                    if not self.color_left:
                        self.color_left = self.robot.get_color()
                        self.robot.turn_for(30, 0, 2)
                    if not self.color_right:
                        self.color_right = self.robot.get_color()
                        self.robot.turn_for(0, 30, 1)
                    else:
                        self.turning = False
                        return Status.SUCCESS
                elif not self.left_done:
                    self.robot.turn_for(0, 30, 1)
                    self.turning = True
            return Status.RUNNING
        else:
            return Status.INVALID

    def terminate(self, new_status):
        if new_status == Status.SUCCESS:
            bb = Blackboard()
            bb.set("biome_type", analyze_type(bb.get("biome_type"),
                                              self.color_original,
                                              self.color_left,
                                              self.color_right))
            bb.set("biome_check", False)

from ev3dev2.led import Leds
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B

class Robot:

    def __init__(self):
        self.leds = Leds()
        self.tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
        self.moving = False

    def set_leds(self, color):
        self.leds.set_color("LEFT", color)
        self.leds.set_color("RIGHT", color)

    def move_forward(self, speed=100):
        self.tank_drive.on(speed,speed)

    def stop(self, brake=True):
        self.tank_drive.off(brake)

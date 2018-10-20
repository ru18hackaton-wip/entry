from ev3dev2.led import Leds
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B
from ev3dev2.sensor.lego import UltrasonicSensor

class Robot:

    def __init__(self):
        self.leds = Leds()
        self.tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
        self.moving = False
        self.ultra = UltrasonicSensor()

    def set_leds(self, color):
        self.leds.set_color("LEFT", color)
        self.leds.set_color("RIGHT", color)

    def move(self, speed_left=100, speed_right=100):
        self.tank_drive.on(speed_left,speed_right)

    def stop(self, brake=True):
        self.tank_drive.off(brake)

    def get_distance(self):
        return self.ultra.distance_centimeters

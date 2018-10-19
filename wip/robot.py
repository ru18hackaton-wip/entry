from ev3dev2.led import Leds

class Robot:

    def __init__(self):
        self.leds = Leds()

    def set_leds(self, color):
        self.leds.set_color("LEFT", color)
        self.leds.set_color("RIGHT", color)

from ev3dev2.led import Leds

class Robot:

    def __init__(self):
        self.leds = Leds()

    def xmas(self):
        self.leds.set_color("LEFT", "GREEN")
        self.leds.set_color("RIGHT", "RED")
        self.leds.set_color("LEFT", "RED")
        self.leds.set_color("LEFT", "YELLOW")
        self.leds.set_color("RIGHT", "YELLOW")
        self.leds.set_color("RIGHT", "GREEN")
        self.leds.set_color("LEFT", "GREEN")
        self.leds.set_color("RIGHT", "RED")
        self.leds.set_color("LEFT", "RED")
        self.leds.set_color("LEFT", "YELLOW")
        self.leds.set_color("RIGHT", "YELLOW")
        self.leds.set_color("RIGHT", "GREEN")

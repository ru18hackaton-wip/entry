from ev3dev2.led import Leds
from ev3dev2.motor import MoveTank, OUTPUT_A, OUTPUT_B, LargeMotor
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.sound import Sound

class Robot:

    def __init__(self):
        self.leds = Leds()
        self.tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
        self.tank_drive.set_polarity(LargeMotor.POLARITY_INVERSED)
        self.color = ColorSensor()
        self.ultra = UltrasonicSensor()
        self.sound = Sound()

    def set_leds(self, color):
        self.leds.set_color("LEFT", color)
        self.leds.set_color("RIGHT", color)

    def move(self, speed_left=100, speed_right=100):
        self.tank_drive.on(speed_left,speed_right)

    def stop(self, brake=True):
        self.tank_drive.off(brake)

    def get_distance(self):
        return self.ultra.distance_centimeters

    def get_color(self):
        return self.color.reflected_light_intensity

    def speak(self, say):
        self.sound.speak(text=say, play_type=Sound.PLAY_NO_WAIT_FOR_COMPLETE)

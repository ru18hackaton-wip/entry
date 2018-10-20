#!/usr/bin/env python3
__author__ = "bythew3i"

import evdev
import ev3dev.auto as ev3
import threading


def scale(val, src, dst):
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

def scale_stick(value):
    return scale(value, (0,255),(-100,100))


# ps4 controller set up
print("Finding ps4 controller...")
devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
ps4dev = devices[0].fn

gamepad = evdev.InputDevice(ps4dev)
running = True



# wheel set up
wheel_speed = 0

class MotorThread(threading.Thread):
    def __init__(self):
        self.motor = ev3.LargeMotor(ev3.OUTPUT_A)
        threading.Thread.__init__(self)

    def run(self):
        print("Wheels Ready...")
        while running:
            self.motor.run_direct(duty_cycle_sp=wheel_speed)

        self.motor.stop()

motor_thread = MotorThread()
motor_thread.setDaemon(True)
motor_thread.start()


# steer set up
steer_speed = 0

class DirectionThread(threading.Thread):
    def __init__(self):
        self.motor = ev3.MediumMotor(ev3.OUTPUT_D)
        threading.Thread.__init__(self)

    def run(self):
        print("Steer Ready...")
        while running:
            self.motor.run_direct(duty_cycle_sp=steer_speed)

steer_thread = DirectionThread()
steer_thread.setDaemon(True)
steer_thread.start()


# event listner
for event in gamepad.read_loop():   #this loops infinitely
    print(event.type)
    if event.type == 3:             #A stick is moved
        if event.code == 5:         #Y axis on right stick
            wheel_speed = scale_stick(event.value)
        if event.code == 0:
            steer_speed = scale_stick(event.value)/3.0

    if event.type == 1 and event.code == 302 and event.value == 1:
        print("X button is pressed. Stopping.")
        running = False
        break


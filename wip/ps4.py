#!/usr/bin/env python3
__author__ = "bythew3i"

import evdev

from ev3dev2.motor import MoveJoystick, LargeMotor, OUTPUT_A, OUTPUT_D

def find_controller():
    # ps4 controller set up
    print("Finding ps4 controller...")
    devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]
    ps4dev = devices[0].fn

    gamepad = evdev.InputDevice(ps4dev)
    return gamepad

def create_steering_tank():
    jmove = MoveJoystick(OUTPUT_A, OUTPUT_D)
    jmove.set_polarity(LargeMotor.POLARITY_INVERSED)
    return jmove


def scale(val, src, dst):
    return (float(val - src[0]) / (src[1] - src[0])) * (dst[1] - dst[0]) + dst[0]

def scale_stick(value):
    return scale(value, (0,255),(-100,100))



gamepad = find_controller()
bot = create_steering_tank()

for event in gamepad.read_loop():   #this loops infinitely
    print(event)
    print(repr(event))
    if event.type == 3:             #A stick is moved
        if event.code == 5:         #Y axis on right stick
            wheel_speed = scale_stick(event.value)
        if event.code == 0:
            steer_speed = scale_stick(event.value)/3.0

    if event.type == 1 and event.code == 302 and event.value == 1:
        print("X button is pressed. Stopping.")
        running = False
        break

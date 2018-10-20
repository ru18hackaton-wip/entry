from .main import main

import sys, os.path
FAKE_SYS = os.path.join(os.path.dirname(__file__), '..', 'ev3dev-lang-fake-sys')

sys.path.append(FAKE_SYS)
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from populate_arena import populate_arena
from clean_arena    import clean_arena

import ev3dev2
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.motor import \
    Motor, MediumMotor, LargeMotor, \
    MoveTank, MoveSteering, MoveJoystick, \
    SpeedPercent, SpeedDPM, SpeedDPS, SpeedRPM, SpeedRPS, SpeedNativeUnits, \
    OUTPUT_A, OUTPUT_B

ev3dev2.Device.DEVICE_ROOT_PATH = os.path.join(FAKE_SYS, 'arena')

_internal_set_attribute = ev3dev2.Device._set_attribute
def _set_attribute(self, attribute, name, value):
    # Follow the text with a newline to separate new content from stuff that
    # already existed in the buffer. On the real device we're writing to sysfs
    # attributes where there isn't any persistent buffer, but in the test
    # environment they're normal files on disk which retain previous data.
    attribute = _internal_set_attribute(self, attribute, name, value)
    attribute.write(b'\n')
    return attribute
ev3dev2.Device._set_attribute = _set_attribute

_internal_get_attribute = ev3dev2.Device._get_attribute
def _get_attribute(self, attribute, name):
    # Split on newline delimiter; see _set_attribute above
    attribute, value = _internal_get_attribute(self, attribute, name)
    return attribute, value.split('\n', 1)[0]
ev3dev2.Device._get_attribute = _get_attribute

def dummy_wait(self, cond, timeout=None):
    pass

Motor.wait = dummy_wait

def main_docker():
    clean_arena()
    populate_arena([('large_motor', 0, 'outA'),('large_motor', 1, 'outB'),('ultrasonic_sensor', 0, 'in2'),('color_sensor', 1, 'in3')])
    main()

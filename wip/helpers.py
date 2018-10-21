from enum import Enum

class Biome(Enum):
    FLOOR = 0
    BRIDGE = 1
    LINE = 2
    LINE_LEFT = 3
    LINE_RIGHT = 4

# Checks if color1 and color2 are the same color

def new_biome(color1, color2):
    return not same_biome(color1, color2)

# Returns true if color1-color2 is smaller than 5

def same_biome(color1, color2):
    return abs(color1-color2) < 5

# Tells the robot what type of surface it is on

def analyze_type(prev_type, original, left, right):
    if same_biome(left, right):
        if same_biome(original, left):
            if prev_type == Biome.FLOOR:
                return Biome.BRIDGE
            else:
                return Biome.FLOOR
        else:
            return Biome.LINE
    elif same_biome(left, original):
        return Biome.LINE_LEFT
    elif same_biome(right, original):
        return Biome.LINE_RIGHT

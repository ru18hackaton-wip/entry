from enum import Enum

class Biome(Enum):
    FLOOR = 0
    BRIDGE = 1
    LINE = 2
    LINE_LEFT = 3
    LINE_RIGHT = 4

def new_biome(color1, color2):
    return not same_biome(color1, color2)

def same_biome(color1, color2):
    return abs(color1-color2) < 5

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

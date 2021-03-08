from math import sqrt

FLOAT_ERROR_RATE: float = 1e-6


def floatCompare(a: float, b:float):
    if abs(a - b) < FLOAT_ERROR_RATE:
        return 1
    else:
        return 0

# For tuple/list dotTypes
def dotDistance2(dot1, dot2) -> float:
    return sqrt((dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2)


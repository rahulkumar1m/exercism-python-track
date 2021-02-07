import math

def score(x : int, y : int) -> int:
    circle = math.sqrt(x**2 + y**2)

    if circle <= 1:
        return 10
    elif circle <= 5:
        return 5
    elif circle <= 10:
        return 1
    else:
        return 0

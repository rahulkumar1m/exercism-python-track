def equilateral(sides):
    if (min(sides) <= 0) | (sides[0] + sides[1] <= sides[2]) | (sides[1] + sides[2] <= sides[0]) | (sides[2] + sides[0] <= sides[1]):
        return False
    else:
        return (sides[0] == sides[1]) & (sides[1] == sides[2])


def isosceles(sides):
    if (min(sides) <= 0) | (sides[0] + sides[1] <= sides[2]) | (sides[1] + sides[2] <= sides[0]) | (sides[2] + sides[0] <= sides[1]):
        return False
    else:
        return (sides[0] == sides[1]) | (sides[1] == sides[2]) | (sides[2] == sides[0])


def scalene(sides):
    if (min(sides) <= 0) | (sides[0] + sides[1] <= sides[2]) | (sides[1] + sides[2] <= sides[0]) | (sides[2] + sides[0] <= sides[1]):
        return False
    else:
        return (sides[0] != sides[1]) & (sides[1] != sides[2]) & (sides[2] != sides[0])

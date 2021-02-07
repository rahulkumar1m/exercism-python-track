def square(number):
    if (number > 0) & (number <= 64):
        return 2**(number-1)
    else:
        raise ValueError("Negative Numbers or Numbers > 64 not allowed")


def total():
    return int(sum([2**(number) for number in range(64)]))

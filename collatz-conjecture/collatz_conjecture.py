def steps(number: int) -> int:
    if number <= 0:
        raise ValueError("Negative Number is not allowed")

    if number == 1:
        return 0
    elif number % 2 == 0:
        return steps(number/2) + 1
    else:
        return steps(3 * number + 1) + 1

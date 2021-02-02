def square_of_sum(number: int) -> int:
    return (((number+1)*number)/2)**2


def sum_of_squares(number: int) -> int:
    return sum([x**2 for x in range(number+1)])


def difference_of_squares(number: int) -> int:
    return square_of_sum(number) - sum_of_squares(number)

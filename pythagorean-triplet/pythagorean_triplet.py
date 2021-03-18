def triplets_with_sum(number: int):
    return [[a, b, number - a - b] for a in range(number // 3) for b in range(a + 1, number // 2) if a**2 + b**2 == (number-a-b)**2]

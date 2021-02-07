def palindrome(min_factor, max_factor, largest):
    if min_factor > max_factor:
        raise ValueError(ValueError)

    args = (max_factor ** 2, min_factor**2 + 1, -1) if largest else (min_factor**2, max_factor**2+1)
    palin, factors = None, []
    for num in range(*args):
        if str(num) == str(num)[::-1]:
            valid = False
            for i in range(min_factor, max_factor + 1):
                if num % i == 0 and i <= (num // i) <= max_factor:
                    factors.append([i, num // i])
                    palin, valid = num, True
            if valid:
                break

    return palin, factors

def largest(min_factor, max_factor):
    return palindrome(min_factor, max_factor, largest=True)


def smallest(min_factor, max_factor):
    return palindrome(min_factor, max_factor, largest=False)
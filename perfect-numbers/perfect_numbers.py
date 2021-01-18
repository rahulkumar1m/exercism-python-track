def classify(number):
    if number < 1:
        raise ValueError("Classification is not possible")
    
    factors = [a for a in range(1, int(number/2)+1) if number % a == 0]

    if sum(factors) == number:
        return "perfect"
    elif sum(factors) > number:
        return "abundant"
    else:
        return "deficient"

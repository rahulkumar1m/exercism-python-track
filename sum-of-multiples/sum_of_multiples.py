def sum_of_multiples(limit : int, multiples)-> int:
    # Initializing a set a to store all the mutiples 
    multiple_set = set()

    # Remove non-positive numbers from mutiple list
    multiples = [x for x in multiples if x > 0]

    # calculating all the mutiples
    for i in range(limit):
        for j in multiples:
            if i % j == 0:
                multiple_set.add(i)
                break

    return sum(multiple_set)

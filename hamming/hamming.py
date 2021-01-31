def distance(strand_a : str, strand_b : str) -> int:
    # Raise ValueErrors if length of passed DNA sequences do not match
    if len(strand_a) != len(strand_b):
        raise ValueError("Length of DNA sequences DO NOT MATCH")
    
    # Initializing hammin_distance with 0
    hamming_distance = 0
    
    # Checking for differences between the two sequences
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            hamming_distance += 1
    
    return hamming_distance

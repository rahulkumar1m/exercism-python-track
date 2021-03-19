def primes(limit: int):
    prime = [True for i in range(limit+1)]
    p = 2
    while(p**2 <= limit):
        if prime[p] == True:
            for i in range(p**2, limit + 1, p):
                prime[i] = False
        p += 1
    
    return [p for p in range(2, limit + 1) if prime[p] == True]

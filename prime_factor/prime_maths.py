def max_prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d += 1
        if d*d > n:
            if n > 1: factors.append(n)
            break
    return max(factors)

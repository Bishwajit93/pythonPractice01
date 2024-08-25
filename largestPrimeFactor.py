def prime_factors(n):

    factors = []

    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2
    
    if n > 1:
        factors.append(n)
    
    return factors

number = 600_851_475_143
all_factors = prime_factors(number)
largest_prime_factor = max(all_factors)

print("Prime factors:", all_factors)
print("Largest prime factor:", largest_prime_factor)

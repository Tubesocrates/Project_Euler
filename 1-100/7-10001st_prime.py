import itertools, math, numpy, sympy, functools

from helpers import prime_tests
# analytics.monitor()

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

test = 10001
primes = prime_tests.primesfrom3to(10001)
primes.insert(0, 2)
while len(primes) < test:
    old_last_prime = primes[-1]
    new_last_prime = sympy.nextprime(old_last_prime)
    primes.append(new_last_prime)


print(len(primes))
print(primes[-1])
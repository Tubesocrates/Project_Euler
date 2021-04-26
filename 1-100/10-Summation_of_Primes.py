from helpers import prime_tests
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

num = 2000000
# find out why this doesnt work
primes = prime_tests.primesfrom3to(num)
primes2 = prime_tests.primesfrom2to(num)
primes.insert(0, 2)
Sum = 0
for i in primes:
    Sum += i
Sum2 = 0
for i in primes2:
    Sum2 += i

print(len(primes), len(primes2))
print(primes[0], Sum, Sum2)
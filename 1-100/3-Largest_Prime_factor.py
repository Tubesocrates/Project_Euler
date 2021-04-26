import random, math
from helpers import prime_tests, analytics, mathys
analytics.monitor()

# base_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
# filename = "primes"
test = 600851475143
test1 = 83
# print(len(prime_tests.primes))
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

factor_list = []

def main(n):
    pf = set([])
    while n%2==0:
        pf.add(2)
        n //= 2
    for i in range(3,int(n**(.5)),2):
        while n % i == 0:
            pf.add(i)
            n //= i
    if n > 1:
        pf.add(n)
    LPF = sorted(list(pf))
    print(LPF)
    if LPF == n:
        return LPF


print(main(test), analytics.lap(), analytics.maxMem())
 


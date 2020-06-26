import random, math
from helpers import fermat, analytics
analytics.monitor()

base_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
filename = "primes"
test = 600851475143

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

factor_list = []

def main(test):
    primes = fermat.load_primes(filename, base_primes)
    for prime in primes:
        if test % prime == 0:
            if prime not in factor_list:
                factor_list.append(prime)
    return factor_list[-1]

def main2(n):
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
    return sorted(list(pf))

print(main(test), main2(test), analytics.lap(), analytics.maxMem())
    


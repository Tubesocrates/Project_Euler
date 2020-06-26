import random, math
from helpers import fermat, analytics
analytics.monitor()
# see beln lewis's problem one https://github.com/Phyisis/Problems/blob/master/P001.py

base_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
filename = "primes"
test = 600851475143

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

#generate a list of factors, ok
# def factorize(num):
#     place_holder = num
#     prime_factors = []
#     while place_holder != 0:
#         print("no check", place_holder)
#         if place_holder % 2 == 0:
#             place_holder = place_holder - div(place_holder, 2)
#             print("new num", place_holder)
#         else:
#             prime_factors.append(place_holder)
#             place_holder = place_holder - place_holder
#             break
#     return prime_factors

factor_list = []

def main():
    primes = fermat.load_primes(filename, base_primes)
    for prime in primes:
        if test % prime == 0:
            if prime not in factor_list:
                factor_list.append(prime)
    return factor_list[-1]

print(main(), analytics.lap(), analytics.maxMem())
    

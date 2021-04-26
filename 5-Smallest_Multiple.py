import itertools
from helpers import prime_tests
# analytics.monitor()

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def least_common_multiple(list_of_numbers):
    list_of_numbers.sort()
    primes = []
    for i in list_of_numbers:
        if prime_tests.is_prime(i):
            primes.append(i)
    multiple = 1
    for j in primes:
        multiple *= j

    # last_num = list_of_numbers[-1]
    # Max = mathys.factorial(last_num)
    # pot_mult = last_num**2
    # while pot_mult < Max:
    #     temp = []
    #     for j in list_of_numbers:
    #         if pot_mult % j != 0:
    #             pot_mult += 2*3
    #             continue
    #     temp.append(pot_mult)
    #     pot_mult += 2*3
    # return temp
    return primes, multiple

def listy(num):
    i = []
    for _ in range(1,num+1):
        i.append(_)
    return i

def factor_tree(num):
    if not prime_tests.is_prime(num):
        

print(listy(20))
print(least_common_multiple(listy(20)))
print(least_common_multiple(listy(10)))
""" A perfect number is a number for which the sum of its proper divisors is exactly equal 
to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can 
be written as the sum of two abundant numbers. However, this upper limit cannot be 
reduced any further by analysis even though it is known that the greatest number 
that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the 
sum of two abundant numbers.

Deficient numbers are sometimes called defective numbers (Singh 1997). 
Primes, prime powers, and any divisors of a perfect or deficient number are all deficient. 
The first few deficient numbers are
 1, 2, 3, 4, 5, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 19, 21, 22, 23,

"""
import random, math, pickle, numpy, sympy
from helpers import prime_tests, analytics, mathys

limit = 28123

# find the abundant numbers less than this number
# find out numbers that cant be expressed by any combo of these numbers

def divsum(num):
    divsum = 0
    factors = []
    i = 1
    while i < math.sqrt(num):
        if i not in factors:
            if num % i == 0:
                factors.append(i)
                if i != 1:
                    factors.append(int(num/i))
        i += 1
    factors.sort()
    for j in factors:
        divsum += j
    return divsum

def abundant_numbers(limit):
    i = []
    j = 12
    while j < limit:
        if divsum(j) > j:
            i.append(j)
        j += 1
    return i

print(len(abundant_numbers(limit)))


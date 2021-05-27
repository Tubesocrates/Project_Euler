"""
Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair 
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
import random, math, pickle, numpy, sympy
from helpers import prime_tests, analytics, mathys


def div_sum(num):
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

print(div_sum(220))
print(div_sum(284))



def amicable_nums(limit):
    i = 1
    am_nums = []
    while i < limit - 1:
        temp = div_sum(i)
        if (div_sum(temp) == i and i != temp):
            if i not in am_nums:
                am_nums.append(i)
            if temp not in am_nums:
                am_nums.append(temp)
        i += 1
    return sum(am_nums)


print(amicable_nums(10000))


import itertools, math, sympy, functools

from helpers import prime_tests
# analytics.monitor()

"""The sum of the squares of the first ten natural numbers is, f(1**2+2**2+...10**2=385)

The square of the sum of the first ten natural numbers is, f(1+2+...+10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025-385=2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""

Natural_numbers = [i for i in range(1, 101)]

Square_of_sum = sum(Natural_numbers)**2

Sum_of_Squares = sum(x**2 for x in Natural_numbers)

Answer = Square_of_sum - Sum_of_Squares

print(f"{Square_of_sum} - {Sum_of_Squares} = {Answer}")
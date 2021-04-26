"""2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?"""
from helpers import prime_tests
import math
# power rule
# 2^1000 = ((2^10)^10)^10)


print(math.pow(2, 1000))


long_num = pow(2, 1000)
Length = int(math.log10(long_num))+1
digits = []


while long_num:
    digit = long_num % 10
    long_num = long_num // 10
    digits.append(digit)

result = sum(digits)

print(result)
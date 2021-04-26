import itertools
from helpers import analytics
analytics.monitor()
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 
# 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.
# https://projecteuler.net/problem=4

def is_palindromic_num(number):
    reverse = int(str(number)[::-1])
    if reverse == number:
        return True
    else: False

set_list = []
prod = []
palind = []
def find_palindromic_nums():
    #check 900s bc of hunch
    for pair in itertools.permutations(range(900, 1000), 2):
        if set(pair) not in set_list:
            set_list.append(set(pair))
            prod.append(pair[0]*pair[1])
    for i in prod:
        if is_palindromic_num(i):
            palind.append(i)
    palind.sort()
    return palind[-1]

def main():
    x = find_palindromic_nums()
    return x

print(main(), analytics.lap(), analytics.maxMem())



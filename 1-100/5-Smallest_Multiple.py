import itertools, math, sympy, functools

from helpers import prime_tests
# analytics.monitor()

#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
def gcd(a,b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def List_least_common_multiple(*args):
    """Return lcm of args."""
    return functools.reduce(lcm, args)

def listy(num):
    i = []
    for _ in range(1, num + 1):
        i.append(_)
    print(i)
    return i

Max = 20

def prime_list_builder(Max):
    lists = []
    i = 2
    while i < Max + 1:
        primes = []
        y = prime_tests.factor_tree(i)
        for j in y:
            primes.append(j)
            # print("primes", primes)
        i += 1
        lists.append(primes)
    return lists

def countX(List, x):
    count = 0
    for ele in List: 
        if (ele == x): 
            count = count + 1
    return List, (x, count) 

def counter_element_in_sublists(ListofLists):
    counted = []
    for j in ListofLists:
        if j not in counted:
            temp = []
            for i in j:
                if i not in temp:
                    Set = countX(j, i)
                    # if i[1] > 1:
                    counted.append(Set)
                    temp.append(i)
    return counted

def countY(List, y):
    count = 0
    for ele in List: 
        if (ele == y): 
            count = count + 1
    return y, count

def primes_under(Num):
    i = 2
    p = []
    while i < Num:
        if prime_tests.is_prime(i):
            p.append(i)
            i += 1
        else:
            i += 1
    return p

def adder(counted_dictionary):
    Sum = 1
    for key in counted_dictionary:
        Sum *= key**counted_dictionary[key]
    return Sum

def counter2(ListofLists, Number):
    elements = primes_under(Number)
    Num_of_elements = dict(zip(elements, itertools.repeat(1)))
    for j in ListofLists:
        for i in j:
            ele, count = countY(j, i)
            if count > Num_of_elements[ele]:
                Num_of_elements[ele] = count
    return Num_of_elements



        
prymes = prime_list_builder(20)
counted_prymes = counter_element_in_sublists(prymes)
l = [[2,2],[3,3,5],[5,5,5],[7,5,2]]

# print(counter_element_in_sublists(prime_list_builder(20)))
print(prymes)
print(counter_element_in_sublists(l))
# print(counter2(l, 11))
print(counted_prymes)
print(counter2(prymes, 20))

# https://www.calculatorsoup.com/calculators/math/lcm.php
#double checked with the above link using the prime factorization and the below input:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
print(adder(counter2(prymes, 20)))

print(List_least_common_multiple(*range(1, 21)))

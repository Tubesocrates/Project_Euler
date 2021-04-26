import itertools, math, numpy, sympy, functools

from helpers import prime_tests, analytics

analytics.monitor()

"""A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""
Sum = 1000

def is_square(num):
    x = num // 2
    y = set([x])
    while x*x != num:
        x = (x + num //x) // 2
        if x in y:
            return False
        y.add(x)
    return True

def perf_squares(Sum, Floor):
    perf_squares = []
    for i in range(Floor, Sum + 1):
        if is_square(i):
            perf_squares.append(i)
    return perf_squares

# sets = list(itertools.combinations(perf_squares(1000000, 2), 3))

# print(perf_squares(1000000, 2))
def abc_getter(sets):
    i_storer = []
    final = []
    for i in sets:
        Sum = 0
        for j in i:
            Sum += j
        if Sum == 1000:
            i_storer.append(i)
    for finals in i_storer:
        if finals[0]**2 + finals[1]**2 == finals[2]**2:
           final.append(finals)
    return final

def abc_getter_2(sets):
    sets = sorted(sets)
    lists = []
    abc = []
    for i in sets:
        c = math.sqrt(i[2])
        b = math.sqrt(i[1])
        a_2 = i[0]
        if i[0] == (c**2 - b**2) and math.sqrt(a_2) + b + c == 1000:
            lists.append(i)
        # if math.sqrt(a_2) + b + c == 1000:
        #     list
    for j in lists:
        for q in j:
            abc.append(math.sqrt(q))
    return lists, abc

# print(sets)
# print(abc_getter(sets))
# print(abc_getter_2(sets))
# print(i)

def pythagorean_triples(n):
    triples = []
    for i in range(1, int(n/3) + 1):
        for j in range(1 + 1, int(n/2) + 1):
            k = n - i - j
            if (i*i + j*j == k*k):
                List = [i,j,k]
                triples.append(List)
    return triples

print(pythagorean_triples(1000))
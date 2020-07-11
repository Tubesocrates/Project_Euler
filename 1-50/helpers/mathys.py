import random, math, pickle

def factorial(x):
    total=1
    while x>0:
        total=x*total
        x-=1
    return total

# credit to nullptr https://stackoverflow.com/questions/30226094/how-do-i-decompose-a-number-into-powers-of-2
def power_finder(x):
    powers = []
    i = 1
    while i <= x:
        if i & x:
            powers.append(i)
        i <<= 1
    return powers

def d_and_r_finder(x):
    powers = power_finder(x)
    D = []
    r = []
    for i in powers:
        if x//i == x/i:
            if x//i % 2 != 0:
                D.append(int(x//i))
    for d in D:
        r.append(math.log2((x)//d)/math.log2(2))
    return D[0], r[0]


print(d_and_r_finder(220))
print(math.log2(2))
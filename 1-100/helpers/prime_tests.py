import random, math, pickle, numpy, sympy
from primesieve import *
# https://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
# https://plus.maths.org/content/os/issue50/features/havil/index 
#time the function****

base_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
checked_primes = []

filename = "primes"

# checks to see if a prime file exists, creates one with base primes if it doesn't
def load_primes(filename, base_primes):
    try:
        with open(f"{filename}.pickle", "rb") as f:
            #  this skips loading base primes if it exists
            primes = pickle.load(f)
            # print("loaded")
    except (OSError, IOError) as e:
        primes = pickle.dump(base_primes, open(f"{filename}.pickle", "wb"))
        # print("dumped base primes")
    return primes

# loads primes from primes.pickle
primes = load_primes(filename, base_primes)

# use at end of run to add primes to file
def update_primes(checked_primes, filename):
    with open(f"{filename}.pickle", "rb") as f:
        primes = pickle.load(f)
        primes.extend(checked_primes)
        primes.sort()
        with open(f"{filename}.pickle", "wb") as e:
            primes = pickle.dump(primes, e)

# Sieve of Eratosthenes

#primesfrom2to
#examples


def primesfrom3to(n):
    """returns an array of primes, 3 <= p , n """
    sieve = numpy.ones(n//3, dtype=numpy.bool) # n//2 gives a rounded devision of n divided by 2 #numpy.ones returns an array of shape and type (shape, dtype)
    for i in range(3, int(n**.5) + 1, 2): #for i in the range of 3 to sqrt(n) + 1, every odd number
        if sieve[i//2]:
            sieve[i*i//2::i] = False #i squared//2, extended slice to cut every i
            # print(i, i*i, i*i//2, sieve[i*i//2::i])
    return list(2*numpy.nonzero(sieve)[0][1::]+1) #2 times every True value plus 1, not including 0
# print(primesfrom3to(45))

#learn later
def primesfrom2to(n):
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = numpy.ones(n//3 + (n%6==2), dtype=numpy.bool)
    for i in range(1,int(n**0.5)//3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[       k*k//3     ::2*k] = False
            sieve[k*(k-2*(i&1)+4)//3::2*k] = False
    return numpy.r_[2,3,((3*numpy.nonzero(sieve)[0][1:]+1)|1)]

# Fermat Primality test
def fermat_primality(pot_prime, filename, primes, rounds):
    primes = primes
    pp = pot_prime
    # check prime list
    if is_prime(pp):
        return True
    else:
        # number of tests
        test_num = rounds
        # choose test_num amount of numbers less than the pp, randomly
        random_numbers = []
        for i in range(test_num):
            random_number = random.randint(2, pp-1)
            random_numbers.append(random_number)
        # build checks, if the length of the checks is == to the test_num, then this number is likely prime # (20 chosen for high likelihood of being prime)
        check = []
        for a in random_numbers:
            if math.gcd(a, pp) == 1:
                if pow(a, pp-1, pp) == 1:
                    check.append(a)
        if len(check) > test_num-1:
            checked_primes.append(pp)
            return True, "number is prime, added to the list"
        else:
            return False, "number is not prime"

def add_primes_fermat(primes, new_number):
    primes.sort
    old_largest_prime = primes[-1]
    if new_number not in primes:
        for i in range(old_largest_prime, new_number):
            fermat_primality(i, filename, primes, 20)
        update_primes(checked_primes, filename)
    else:
        pass

#cheats from Phyisis -> https://github.com/Phyisis

# credit to nullptr https://stackoverflow.com/questions/30226094/how-do-i-decompose-a-number-into-powers-of-2
#Miller-Rabin Primality Test
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

def miller_rabin_primality(pot_prime, filename, primes, rounds):
    primes = primes
    pp = pot_prime
    if is_prime(pp): # check prime list
        return True
    else: # test it
        d, r = d_and_r_finder(pp - 1) # write n as (2^r)*d + 1 with d as odd (by factoring out powers of 2 from n - 1)
        test_num = rounds # number of rounds of testing to perform
        random_numbers = []
        for i in range(test_num):
            random_number = random.randint(2, pp-2)
            random_numbers.append(random_number)
        for a in random_numbers:
            x = pow(a,d,pp)
            if x == 1 or x == pp - 1:
                continue
            y = True
            for _ in range(int(r) - 1):
                x = pow(x,2,pp)
                if x == pp - 1:
                    y = False
                    break
            if y:
                return False
        checked_primes.append(pp)
        return True

def add_primes_M_R(primes, new_number):
    primes.sort
    old_largest_prime = primes[-1]
    if new_number not in primes:
        for i in range(old_largest_prime, new_number):
            miller_rabin_primality(i, filename, primes, 20)
        update_primes(checked_primes, filename)
    else:
        pass

#can only check list of primes
def is_prime(number):
    value = False
    if number in primes:
        value = True
    return value

# prime facorization with LCM
def prime_factors(number):
    for i in range(number):
        if not is_prime(i):
            pass
    # build

def Largest_Prime_factor(test, primes):
    factor_list = []
    primes = primes
    for prime in primes:
        if test % prime == 0:
            if prime not in factor_list:
                factor_list.append(prime)
    factor_list.sort()
    return factor_list[-1]

def Smallest_Prime_factor(test, primes):
    factor_list = []
    primes = primes
    for prime in primes:
        if test % prime == 0:
            if prime not in factor_list:
                factor_list.append(prime)
    factor_list.sort()
    return factor_list[0]

def factor_tree(num):
    factors = []
    Num = num
    primes = primesfrom2to(num)
    # print("*"*5, "FACTOR TREE", "*"*5)
    while not is_prime(Num):
        x = Smallest_Prime_factor(Num, primes)
        Numb = Num // x
        # print(f"{x} | {Num}", end = '')
        # print("\n  ", "-"*5)
        # print(f"   {Numb}")
        Num = Numb
        factors.append(x)
    else:
        Numb = num
    # print(f"   {Numb}")
    factors.append(Num)
    # print("factor list:", factors)
    # print("\t  ", "END")
    return factors


# print(factor_tree(2940))
# print(factor_tree(3150))

def LCM(list_of_numbers):
    for _ in list_of_numbers:
        factor_tree(_)
        #compare list of numbers blah blah blah

# def GCF(list):
#     for pair in itertools.permutations(list, 2):
#         if pair

# print(miller_rabin_primality(10010111, filename, primes, 20))
# add_primes_M_R(primes, 10010111)
# print(miller_rabin_primality(479001599, filename, primes, 20))
# add_primes_M_R(primes, 479001599)
# print(miller_rabin_primality(1012356487, filename, primes, 100))
# add_primes_M_R(primes, 1012356487)
# print(fermat_primality(10010111, filename, primes, 20))
# add_primes_fermat(primes, 10010111)
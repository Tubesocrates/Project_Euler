import random, math, pickle
from helpers import analytics, mathys
#time the function****

base_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
checked_primes = []

filename = "primes"

# checks to see if a prime file exists, creates one with base primes if it doesn't
def load_primes(filename, base_primes):
    try:
        with open(f"{filename}.pickle", "rb") as f:
            # note this skips loading base primes if it exists
            primes = pickle.load(f)
            print("loaded")
    except (OSError, IOError) as e:
        primes = pickle.dump(base_primes, open(f"{filename}.pickle", "wb"))
        print("dumped base primes")
    return primes

primes = load_primes(filename, base_primes)

# use inside prime checker to add primes to file
def update_primes(found_prime, filename):
    with open(f"{filename}.pickle", "rb") as f:
        primes = pickle.load(f)
        # print("loaded previous primes")
        primes.append(found_prime)
        # print(primes)
        with open(f"{filename}.pickle", "wb") as e:
            primes = pickle.dump(primes, e)
            # print("dumped, new prime list")

# Fermat Primality test
def ferm_primality(pot_prime, filename, primes, rounds):
    # loads primes from primes.pickle
    primes = primes
    pp = pot_prime
    # check prime list
    if pp in primes:
        # print(f"number {pp} is already in list... next")
        return True, "number is prime"
    else:
        # test it
        # number of tests
        test_num = rounds
        # choose test_num amount of numbers less than the pp, randomly
        random_numbers = []
        for i in range(test_num):
            random_number = random.randint(2, pp-1)
            random_numbers.append(random_number)
        # build checks, if the length of the checks is == to the test_num, then this number is likely prime 
        # (20 chosen for high likelihood of being prime)
        check = []
        for a in random_numbers:
            if math.gcd(a, pp) == 1:
                if a**(pp-1) % pp == 1:
                    check.append(a)
        # print("pp, check, len(check):", pp, check, len(check))
        if len(check) > test_num-1:
            checked_primes.append(pp)
            # print(f"cheked all {len(check)} numbers...")
            # print(f"{pp} added to the list")
            update_primes(pp, filename)
            return True, "number is prime, added to the list"
        else:
            return False, "number is not prime"

#Miller-Rabin Primality Test
def miller_rabin_primality(pot_prime, filename, primes, rounds):
    # loads primes from primes.pickle
    primes = primes
    pp = pot_prime
    # check prime list
    if pp in primes:
        # print(f"number {pp} is already in list... next")
        return True, "number is prime"
    else:
        # test it
        # write n as (2^r)*d + 1 with d as odd ( by factoring out powers of 2 from n - 1)
        d, r = mathys.d_and_r_finder(pp - 1)
        # number of rounds of testing to perform
        test_num = rounds
        random_numbers = []
        for i in range(test_num):
            random_number = random.randint(2, pp-2)
            random_numbers.append(random_number)
        # build checks, if the length of the checks is == to the test_num, then this number is likely prime 
        # (20 chosen for high likelihood of being prime)
        check = []
        for a in random_numbers:
            x = a**d % pp
            if x = 1 or x = pp - 1:
                while len(check) < r - 1:
                    x = x**2 % pp
                    check.append(x)
                    if x = pp - 1:
                        


        # print("pp, check, len(check):", pp, check, len(check))
        if len(check) > test_num-1:
            checked_primes.append(pp)
            # print(f"cheked all {len(check)} numbers...")
            # print(f"{pp} added to the list")
            update_primes(pp, filename)
            return True, "number is prime, added to the list"
        else:
            return False, "number is not prime"

def add_primes(old_largest_prime, new_number):
    for i in range(old_largest_prime, new_number):
        ferm_primality(i, filename, primes, 20)






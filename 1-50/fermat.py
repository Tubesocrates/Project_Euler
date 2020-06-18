import random, math, pickle


base_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
checked_primes = []
filtered_check_primes = []

filename = primes

# Fermat Primality test
def ferm_primality_num(pot_prime, checked_primes, filtered_check_primes):
    cp, fp = filtered_check_prime(checked_primes, filtered_check_primes)
    pp = pot_prime
    # check prime list
    if pot_prime in cp or pot_prime in base_primes:
        print("number in list... next")
        return True, "number is prime"
    else:
        # test it
        # number of tests
        test_num = 20
        # build random numbers for check
        random_numbers = []
        for i in range(test_num):
            random_number = random.randint(2, pp-1)
            random_numbers.append(random_number)
        #build checks
        check = []
        for a in random_numbers:
            if math.gcd(a, pp) == 1:
                if a**(pp-1) % pp == 1:
                    check.append(a)
        print("pp, check, len(check):", pp, check, len(check))
        if len(check) > test_num-1:
            checked_primes.append(pp)
            print("cheked numbers... all", len(check))
            print(f"{pp} added to the list")
            return True, "number is prime, added to the list"
        else:
            return False, "number is not prime"

def filtered_check_prime(checked_primes, filtered_check_primes):
    # print("filtered checked primes, checked primes", filtered_check_primes, checked_primes)
    if len(filtered_check_primes) == 0:
        i = 0
        while i < len(checked_primes):
            print(checked_primes[i])
            I = checked_primes[i]
            if I % 2 == 0:
                print("do 2")
                checked_primes.pop(i)
                filtered_check_primes.append(i)
            elif I % 3 == 0:
                print("do 3")
                checked_primes.pop(i)
                filtered_check_primes.append(i)
            elif I % 5 == 0:
                print("do 5")
                checked_primes.pop(i)
                filtered_check_primes.append(i)
            i += 1
        print("post filter", filtered_check_primes, checked_primes)
    return checked_primes, filtered_check_primes


def true_primes():
    pass

for i in range(29, 42):
    ferm_primality_num(i, checked_primes, filtered_check_primes)


print(ferm_primality_num(13195, checked_primes, filtered_check_primes))

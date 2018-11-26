import math
import time

def is_prime(x):
    d = 2 # divisor
    while d <= int(math.sqrt(x)):
        if x%d == 0: # remainder of x/d
            return False
        elif d >= int(math.sqrt(x)):
            return True
        else:
            d += 1

def generate_primes(n):
    start = time.time()
    print(2)
    print(3)
    i = 2 # primes generated
    x = 5 # first integer tested
    while i < n:
        if is_prime(x) is True:
            print(x)
            i += 1
            x += 2
        else:
            x += 2

    end = time.time()
    time_taken = end - start
    print(str(n) + " primes were generated in " + str(time_taken) + "s.")

def lucas_lehmer(p): # Lucas-Lehmer test if 2^p - 1 is prime
    s = 4
    M = 2**p - 1
    for x in range(0, p-2):
        s = (s**2 - 2)%M
    if s == 0:
        return True
    else:
        return False
    
def generate_mersenne(n):
    start = time.time()
    print(3)
    i = 1 # primes generated
    p = 3 # first exponent tested
    while i < n:
        if lucas_lehmer(p) is True:
            print(2**p - 1)
            i += 1 # 1 prime created
            p += 1 # test next exponent
        else:
            p += 1

    end = time.time()
    time_taken = end - start
    print(str(n) + " Mersenne primes were generated in " + str(time_taken) + "s.")

mode = 0

while True:
    if mode == 0:
        print('1. Primality Test')
        print('2. Generate Primes')
        print('3. Generate Mersenne Primes')
        mode = int(input('Mode: '))
    elif mode == 1: # Primality Test
        test = int(input('Input: '))
        if is_prime(test) is True:
            print(str(test) + ' is prime!')
        elif is_prime(test) is False:
            print(str(test) + ' is not prime!')
        else:
            print('Invalid input.')
        _return = str(input('Return to main menu? Y/N '))
        if _return == 'Y' or _return == 'y':
            mode = 0
    elif mode == 2: # Generate Primes
        n = int(input('n? '))
        generate_primes(n)
        _return = str(input('Return to main menu? Y/N '))
        if _return == 'Y' or _return == 'y':
            mode = 0
    elif mode == 3: # Generate Mersenne Primes
        n = int(input('n? '))
        generate_mersenne(n)
        _return = str(input('Return to main menu? Y/N '))
        if _return == 'Y' or _return == 'y':
            mode = 0
    else: # Invalid input
        print('Invalid input.')
        mode = 0

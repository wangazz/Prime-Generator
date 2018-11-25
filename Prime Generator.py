import time

def is_prime(x):
    d = 2 # divisor
    while d <= x//2:
        if x/d == x//d:
            return False
        elif d == x//2:
            return True
        else:
            d += 1

def generate_primes(n):
    start = time.time()
    i = 0 # primes generated
    x = 2 # first integer tested

    while i < n:
        if is_prime(x) is True:
            print(x)
            i += 1 # 1 prime created
            x += 1 # test next integer
        else:
            x += 1

    end = time.time()
    time_taken = end - start
    print(str(n) + " primes were generated in " + str(time_taken) + "s.")

def generate_mersenne(n):
    start = time.time()
    i = 0 # primes generated
    x = 2 # first integer tested

    while i < n:
        if is_prime(2**x - 1) is True:
            print(2**x - 1)
            i += 1 # 1 prime created
            x += 1 # test next integer
        else:
            x += 1

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
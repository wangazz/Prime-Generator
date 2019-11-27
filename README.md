# Prime-Generator
C# console app with functions for primality testing, prime generation, and Mersenne prime generation.

This was originally a Python script, but has been migrated to C# for performance improvements.

The current program implements a trial division algorithm for primality testing, and a Lucas-Lehmer algorithm for generating Mersenne primes.

On a Microsoft Surface Book, this script generates the first 10,000 prime numbers in 4.78 seconds. The first 16 Mersenne primes are generated in under 30 seconds. 

Future updates may focus on:
- Speed improvements
- Support for other types of primes

Known issues include:
- 2 is not recognised as a prime number by the primality testing function and is hardwired into the generation algorithm

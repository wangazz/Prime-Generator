﻿using System;

namespace Prime_Generator_CSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            int mode = 0;
            
            while(true) {
                mode = primeGeneratorProgram(mode);
            }
        }

        private static int primeGeneratorProgram(int mode) {
            if (mode == 0) { // Select Mode
                Console.WriteLine("1. Primality Test");
                Console.WriteLine("2. Generate Primes");
                Console.WriteLine("3. Generate Mersenne Primes");
                Console.WriteLine("Select Mode: ");
                return Convert.ToInt32(Console.ReadLine());
            } 
            else if (mode == 1) { // Primality Test
                Console.WriteLine("Input?");
                int intToTest = Convert.ToInt32(Console.ReadLine());
                bool result = isPrime(intToTest);

                if (result == true) {
                    Console.WriteLine(intToTest + " is prime!");
                } 
                else if (result == false) {
                    Console.WriteLine(intToTest + " is not prime!");
                } 
                else {
                    Console.WriteLine("Invalid input.");
                }

                return 0;
            } 
            else if (mode == 2) { // Generate Primes
                Console.WriteLine("n? ");
                int n = Convert.ToInt32(Console.ReadLine());
                generatePrimes(n);
                return 0;
            } 
            else if (mode == 3) {// Generate Mersenne Primes
                Console.WriteLine("n? ");
                int n = Convert.ToInt32(Console.ReadLine());
                generateMersennePrimes(n);
                return 0;
            } 
            else { // Invalid Input
                Console.WriteLine("Invalid input.");
                return 0;
            }
        }

        private static Boolean isPrime(int x) {
            int d = 2;

            while (d <= Math.Floor((Math.Sqrt(x)))) {
                if (x % d == 0) {
                    return false;
                } 
                else {
                    d++;
                }
            }

            return true;
        }

        private static Boolean lucasLehmerTest(int p) {
            double s = 4;
            double m = Math.Pow(2,p) - 1;

            for (int x = 0; x < p-2; x++) {
                s = (Math.Pow(s,2) - 2) % m;
            }
            if (s == 0) {
                return true;
            } 
            else {
                return false;
            }
        }

        private static void generatePrimes(int primesToGenerate) {
            Console.WriteLine(2);
            Console.WriteLine(3);

            int primesGenerated = 2;
            int integerToTest = 5;

            while (primesGenerated < primesToGenerate) {
                if (isPrime(integerToTest) == true) {
                    Console.WriteLine(integerToTest);
                    primesGenerated++;
                    integerToTest += 2;
                }
                else {
                    integerToTest += 2;
                }
            }

            Console.WriteLine(primesToGenerate + " primes were generated.");
        }

        private static void generateMersennePrimes(int primesToGenerate) {
            Console.WriteLine(3);
            int primesGenerated = 1;
            int p = 3;

            while (primesGenerated < primesToGenerate) {
                if (lucasLehmerTest(p) == true) {
                    Console.WriteLine(Math.Pow(2,p) - 1);
                    primesGenerated++;
                    p++;
                }
                else {
                    p++;
                }
            }

            Console.WriteLine(primesGenerated + " Mersenne primes were generated.");
        }
    }
}

"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math


def smallest_prime_factor(number):
    for i in range(2, int(number)+1):
        if number % i == 0:
            return i
    
def largest_prime_factor(number):
    quotient = number
    while quotient != 1:
        smallest_prime = smallest_prime_factor(quotient)
        if smallest_prime == quotient:
            return smallest_prime
        quotient = quotient / smallest_prime_factor(quotient)

if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
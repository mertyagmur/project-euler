"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

from math import sqrt

def is_prime(number):
    if (number <= 1):
        return False
    for i in range(2, int(sqrt(number)) + 1):
        if (number % i == 0):
            return False
    return True

def all_primes(ordinal_num):
    prime_numbers = []
    number_to_check_primality = 2
    while (len(prime_numbers) != ordinal_num):
        if is_prime(number_to_check_primality):
            prime_numbers.append(number_to_check_primality)
        number_to_check_primality += 1
    return prime_numbers[-1]


if __name__ == "__main__":
    print(all_primes(10001))
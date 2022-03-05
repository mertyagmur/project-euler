"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025 - 385 = 2640
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def difference(number):

    sum_of_numbers = 0
    sum_of_squares = 0

    for i in range(number + 1):
        sum_of_numbers += i
        sum_of_squares += i ** 2
    return (sum_of_numbers ** 2 - sum_of_squares)


if __name__ == "__main__":
    print(difference(100))
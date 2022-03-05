"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

def is_divisable_by_all(number, range_num):
    for i in range(1, range_num + 1):
        if (number % i != 0):
            return False
    return True

def smallest_divisable_by_all(range_num):
    number = range_num
    while not is_divisable_by_all(number, range_num):
        number += 1
    return number


if __name__ == "__main__":
    print(smallest_divisable_by_all(20))

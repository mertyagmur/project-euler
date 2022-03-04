"""
Problem 1 - Multiples of 3 or 5:
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

multiples_of_three_or_five = [number for number in range(1000) if number % 3 == 0 or number % 5 == 0]

print(sum(multiples_of_three_or_five))
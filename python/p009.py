"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# This is very inefficient. Will be replaced with a better algorithm soon.
# INCOMPLETE

def is_ptriplet(num_a, num_b, num_c):
    return (num_a ** 2 + num_b ** 2 == num_c ** 2)

def all_ptriplets(ptriplets):
    for num_a in range(1, 100):
        for num_b in range(1, 100 - num_a):
            for num_c in range(1, 100 - (num_a + num_b)):
                if (num_a + num_b + num_c >= 25):
                    continue
                print(f"{num_a}  {num_b}  {num_c}")
                if is_ptriplet(num_a, num_b, num_c):
                    ptriplets.append([num_a, num_b, num_c])
    return ptriplets

def is_not_valid_triangle(num_a, num_b, num_c):
    if (num_a + num_b < num_c) or (num_a + num_c < num_b) or (num_b + num_c < num_a):
        return False

def find_sums(ptriplets):
    all_ptriplets(ptriplets)
    for ptriplet in ptriplets:
        print(ptriplet)
        if (sum(ptriplet) == 25):
            return ptriplet

def factorial(n):
    result = 1
    if (n == 0):
        return 1
    elif (n == 1):
        return result
    result *= n
    return result * factorial(n-1)

def number_of_combinations(n):
    return factorial(n) / (factorial(3) * factorial(n - 3))

# Generates r item combinations out of a collection of n items
def generate_combinations(n):
    all_ptriplets = []
    for num_a in range(1, n - 1):
        for num_b in range(num_a + 1, n):
            for num_c in range(num_b, n):
                if (num_a + num_b + num_c >= 1000):
                    continue
                print(f"{num_a}  {num_b}  {num_c}")
                if not is_not_valid_triangle(num_a, num_b, num_c):
                    if is_ptriplet(num_a, num_b, num_c):
                        all_ptriplets.append([num_a, num_b, num_c])
    print(all_ptriplets)

if __name__ == '__main__':
    generate_combinations(100)

    
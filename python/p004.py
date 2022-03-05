"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def is_palindrome(number):
    if (len(str(number)) %2 == 0):
        digits_to_compare = len(str(number)) / 2
        for i in range(int(digits_to_compare)):
            if (str(number)[i] != str(number)[-(i+1)]):
                return False
        return True
    else:
        digits_to_compare = (len(str(number)) - 1) / 2
        for i in range(int(digits_to_compare)):
            if (str(number)[i] != str(number)[-(i+1)]):
                return False
        return True

def largest_palindrome():
    palindromes = []
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            if is_palindrome(i*j):
                palindromes.append(i*j)
    return max(palindromes)

if __name__ == "__main__":
    print(largest_palindrome())
'''
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.
'''

def is_ugly(n: int) -> bool:
    if n == 1:
        return True
    if n % 2 == 0:
        return is_ugly(n // 2)
    if n % 3 == 0:
        return is_ugly(n // 3)
    if n % 5 == 0:
        return is_ugly(n // 5)
    return False

# test is_ugly
print(is_ugly(1))
print(is_ugly(4))
print(is_ugly(10))
print(is_ugly(11))
print(is_ugly(12))
print(is_ugly(13))
print(is_ugly(15))
print(is_ugly(16))
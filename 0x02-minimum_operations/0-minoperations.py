#!/usr/bin/python3
"""Write a method that calculates the fewest number
needed to result in exactly n H characters in the file
"""

def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n //= divisor
            operations += divisor
        else:
            divisor += 1

    return operations

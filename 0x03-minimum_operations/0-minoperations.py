#!/usr/bin/python3
import math


def minOperations(n):
    """ Calculates the fewest number of operations needed to result in
        exactly n H characters
    """
    sum = 0
    if n <= 1:
        return sum
    for i in range(2, int(math.sqrt(n) + 1)):
        while n % i == 0:
            sum += i
            n = n // i
    if n > 1:
        sum += n
    return sum

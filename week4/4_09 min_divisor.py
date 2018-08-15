# 4_09 min_divisor
import math
n = int(input())


def MinDivisor(n):
    q = math.floor(math.sqrt(n))
    i = 2
    while i <= q:
        if n // i == n / i:
            return i
        i = i + 1
    return n

print(MinDivisor(n))

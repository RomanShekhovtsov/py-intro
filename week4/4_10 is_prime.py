# 4_10 is_prime
import math
n = int(input())


def IsPrime(n):
    q = math.sqrt(n)
    i = 2
    while i <= q:
        if n // i == n / i:
            return False
        i = i + 1
    return True

if IsPrime(n):
    print("YES")
else:
    print("NO")

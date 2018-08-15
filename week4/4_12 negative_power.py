# 4_12 negative_power
a = float(input())
n = int(input())


def power(a, n):
    if n == 0:
        return 1

    if a == 0:
        return 0

    res = 1
    i = n
    while i != 0:
        if n > 0:
            res = res * a
            i = i - 1
        else:
            res = 1 / a * res
            i = i + 1
    return res

print(power(a, n))

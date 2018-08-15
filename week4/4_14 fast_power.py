# 4_14 fast_power
a = float(input())
n = int(input())


def power(a, n):
    if n == 0:
        return 1

    if a == 0:
        return 0

    if n > 0:
        if n % 2 == 0:
            return power(a * a, n / 2)
        else:
            return a * power(a, n - 1)
    else:
        return 1 / power(a, -n)

print(power(a, n))

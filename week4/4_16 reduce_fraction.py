# 4_16 reduce_fraction
n, m = int(input()), int(input())


def EuclideNOD(n, m):
    if n > m:
        max = n
        min = m
    else:
        max = m
        min = n

    if max % min == 0:
        return min
    else:
        return EuclideNOD(max % min, min)


def ReduceFraction(n, m):
    nod = EuclideNOD(n, m)
    return n / nod, m / nod

p, q = ReduceFraction(n, m)
print(int(p), int(q))

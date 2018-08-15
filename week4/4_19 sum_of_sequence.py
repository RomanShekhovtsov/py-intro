# 4_19 sum_of_sequence


def sum(s):
    n = int(input())
    if n == 0:
        return s
    else:
        return n + sum(s)

print(sum(0))

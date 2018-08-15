# 4_13 add_without_add


def sum(a, b):
    if a == 0:
        return b

    if b == 0:
        return a

    return 1 + 1 + sum(a - 1, b - 1)

a, b = int(input()), int(input())
print(sum(a, b))

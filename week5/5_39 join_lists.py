# 5_39 join_lists
a = list(map(int, input().split()))
b = list(map(int, input().split()))


def merge(a, b):
    c = []
    a_i = 0
    b_i = 0

    while a_i < len(a):
        if b_i == len(b):
            c.extend(a[a_i:])
            break

        if a[a_i] > b[b_i]:
            c.append(b[b_i])
            b_i = b_i + 1
        else:
            c.append(a[a_i])
            a_i = a_i + 1

    if b_i < len(b):
        c.extend(b[b_i:])

    return c

print(" ".join(str(x) for x in merge(a, b)))

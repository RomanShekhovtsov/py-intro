# 4_20 reverse_of_sequence


def reverse():
    n = int(input())
    if n == 0:
        print(n)
    else:
        reverse()
        print(n)

reverse()

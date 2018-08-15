# 2_16 count of equal
(a, b, c) = (int(input()), int(input()), int(input()))
n = 2
if (a == b) and (b == c) and (a == c):
    n = 3
if (a != b) and (b != c) and (a != c):
    n = 0

print(n)

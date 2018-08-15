# 2_15 order 3 numbers
(a, b, c) = (input(), input(), input())
if a > b:
    (a, b) = (b, a)
if b > c:
    (b, c) = (c, b)
    if a > b:
        (a, b) = (b, a)
print(a, b, c)

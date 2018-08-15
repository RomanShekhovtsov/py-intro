# 1_23 max of two
a = int(input())
b = int(input())
s = a // b
s = (s + 2) % (s + 1)
print(a * s + b * (1 - s))

# 3_12 linear system
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())

x = (f * b - d * e) / (c * b - d * a)
if b == 0:
    y = (f - c * x) / d
else:
    y = (e - a * x) / b
print(x, y)

# 3_xx Gorners scheme
n = int(input())
x = float(input())
s = 0

i = 0
xn = 1.0
while i <= n:
    an = float(input())
    s = s + an * xn
    print(s, an * xn)
    xn = xn * x
    i = i + 1
print( s )

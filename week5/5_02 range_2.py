# 5_02 range_2
a = int(input())
b = int(input())

step = 1
if a > b:
    step = -1

for n in range(a, b + step, step):
    print(n, end=' ')

# 2_45 max number of equals in row
max = 0
curmax = 1
prev = 0
n = -1
while not (n == 0):
    n = int(input())
    if n == 0:
        continue

    if n == prev:
        curmax = curmax + 1
    else:
        curmax = 1

    if curmax > max:
        max = curmax

    prev = n

print(max)

# 2_39 count of equal to max
max = 0
c = 0
n = -1
while not (n == 0):
    n = int(input())
    if n == 0:
        continue

    if n == max:
        c = c + 1

    if n > max:
        max = n
        c = 1

print(c)

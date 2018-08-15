# 2_38 second max
max = 0
secmax = 0
n = -1
while not (n == 0):
    n = int(input())
    if n == 0:
        continue

    if n > max:
        secmax = max
        max = n
        continue

    if n <= max and n > secmax:
        secmax = n

print(secmax)

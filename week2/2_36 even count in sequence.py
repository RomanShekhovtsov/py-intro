# 2_36 even count in sequence
c = 0
n = -1
while not (n == 0):
    n = int(input())
    if n == 0:
        continue
    if n % 2 == 0:
        c = c + 1

print(c)

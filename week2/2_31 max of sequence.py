# 2_31 max of sequence
n = -1
max = -1
while not (n == 0):
    n = int(input())
    if max < n:
        max = n
print(max)

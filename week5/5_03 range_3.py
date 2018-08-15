# 5_03 range_3
n = int(input())

for i in range(10 ** n - 1, 10 ** (n - 1) - 1, -2):
    print(i, end=' ')

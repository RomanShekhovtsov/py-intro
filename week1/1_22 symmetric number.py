# 1_22 symmetric number
n = int(input())
d1 = n // 1000
d2 = (n // 100) % 10
d3 = (n // 10) % 10
d4 = n % 10

n1 = d1 * 10 + d2
n2 = d4 * 10 + d3

diff = n1 - n2
res = diff * diff + 1
print(res)

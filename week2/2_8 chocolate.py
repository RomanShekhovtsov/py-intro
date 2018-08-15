# 2_8 chocolate
n = int(input())
m = int(input())
k = int(input())

r = 'NO'
if (k % n == 0) or (k % m == 0):
    if m * n >= k:
        r = 'YES'
print(r)

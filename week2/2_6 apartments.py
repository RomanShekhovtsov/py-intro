# 2_6 apartments
n1 = int(input())
n2 = int(input())
n = n2 - n1 + 1
r = 'NO'

if n1 > 0 and n2 > 0 and n1 <= 10000 and n2 <= 10000 and n2 > n1:
    if ((n1 % n == 1) and (n2 % n == 0)) or (n1 == 1):
        r = 'YES'

print(r)

# 1_18 clock2
n = int(input())

h = n // 3600 % 24
m = (n // 60) % 60
s = n % 60

print(h, ':', sep='', end='')
print(m // 10, m % 10, ':', sep='', end='')
print(s // 10, s % 10, sep='')

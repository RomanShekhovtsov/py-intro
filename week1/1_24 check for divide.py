# 1_24 check for divide
a = int(input())
b = int(input())
s = a % b
s = (s + 2) % (s + 1)
print('NO' * s + 'YES' * (1 - s))

# 3_07 complex percents
import math
p = int(input())
x = int(input())
y = int(input())
k = int(input())
s = x * 100 + y
i = 0

while i < k:
    s = math.floor(s * (100 + p) / 100)
    i = i + 1
print(s // 100, s % 100)

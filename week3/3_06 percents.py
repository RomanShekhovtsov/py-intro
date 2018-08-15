# 3_6 percents
import math
p = int(input())
x = int(input())
y = int(input())
s = x * 100 + y
r = math.floor(s * (100 + p) / 100)
print(r // 100, r % 100)

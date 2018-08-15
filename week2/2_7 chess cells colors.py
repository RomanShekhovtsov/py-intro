# 2_7 chess cells colors
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1 - x2 + y1 - y2) % 2 == 0:
    r = 'YES'
else:
    r = 'NO'
print(r)

# 2_5 kings move
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1 - x2) < 2 and abs(y1 - y2) < 2:
    r = 'YES'
else:
    r = 'NO'
print(r)

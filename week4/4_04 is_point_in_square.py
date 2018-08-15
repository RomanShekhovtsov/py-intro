# 4_04 is_point_in_square
x = float(input())
y = float(input())


def IsPointInSquare(x, y):
    return -1 <= x <= 1 and -1 <= y <= 1

if IsPointInSquare(x, y):
    print('YES')
else:
    print('NO')

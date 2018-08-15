# 5_26 nearest_number
n = int(input())
lst = map(int, input().split())
x = int(input())

nearest = 9999
for m in lst:
    if abs(nearest - x) > abs(m - x):
        nearest = m

print(nearest)

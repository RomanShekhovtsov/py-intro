# 5_15 count_of_positive
l = map(int, input().split())

count = 0
for i in l:
    if i > 0:
        count = count + 1

print(count)

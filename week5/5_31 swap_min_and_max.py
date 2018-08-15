# 5_31 swap_min_and_max
lst = list(map(int, input().split()))

min_ = lst[0]
max_ = lst[0]
min_i = 0
max_i = 0

i = 1
while i < len(lst):
    if min_ > lst[i]:
        min_ = lst[i]
        min_i = i
    if max_ < lst[i]:
        max_ = lst[i]
        max_i = i
    i = i + 1

lst[min_i] = max_
lst[max_i] = min_
print(' '.join(map(str, lst)))

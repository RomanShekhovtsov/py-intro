# 5_29 swap_neighbors
lst = input().split()

res = []
len_lst = len(lst)
i = 0
while i < len_lst - 1:
    res.extend([lst[i + 1], lst[i]])
    i = i + 2

if len_lst % 2 == 1:
    res.append(lst[len_lst - 1])

print(' '.join(res))

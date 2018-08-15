# 5_43 create_archive
lst = list(map(int, input().split()))
s, n = lst[0], lst[1]

v = []
for i in range(n):
    v.append(int(input()))
v.sort()

users = 0
space = 0
for i in range(n):
    space = space + v[i]
    if space > s:
        break
    users = users + 1

print(users)

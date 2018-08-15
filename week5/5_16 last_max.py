# 5_16 last_max
l = map(int, input().split())

m = None
ind = 0
i = 0
for n in l:
    if m is None:
        m = n

    if n >= m:
        m = n
        ind = i
    i = i + 1

print(m, ind)

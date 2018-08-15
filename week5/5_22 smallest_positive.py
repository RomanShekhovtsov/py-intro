# 5_22 smallest_positive
l = map(int, input().split())

m = None
for n in l:
    if n > 0:
        if m is None:
            m = n

        if n < m:
            m = n

print(m)

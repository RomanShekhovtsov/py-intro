# 5_17 more_than_prev
l = map(int, input().split())

prev = None
for n in l:
    if prev is None:
        prev = n

    if n > prev:
        print(n, end=' ')
    prev = n
print()

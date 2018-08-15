# 5_14 even_elements
l = map(int, input().split())

res = []
for i in l:
    if i % 2 == 0:
        res = res + list((i, ))

print(' '.join(map(str, res)))

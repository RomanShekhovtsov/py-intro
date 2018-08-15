# 2_17 prisoner of castle If
(a, b, c) = (int(input()), int(input()), int(input()))
(d, e) = (int(input()), int(input()))

# ordering a,b,c:
if a > b:
    (a, b) = (b, a)
if b > c:
    (b, c) = (c, b)
    if a > b:
        (a, b) = (b, a)

# ordering d, e:
if d > e:
    (d, e) = (e, d)
# print(a, b, c, d, e)

if a <= d and b <= e:
    r = 'YES'
else:
    r = 'NO'
print(r)

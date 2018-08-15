# 2_18 boxes
(a1, b1, c1) = (int(input()), int(input()), int(input()))
(a2, b2, c2) = (int(input()), int(input()), int(input()))

# ordering 1:
if a1 > b1:
    (a1, b1) = (b1, a1)
if b1 > c1:
    (b1, c1) = (c1, b1)
    if a1 > b1:
        (a1, b1) = (b1, a1)

# ordering 2:
if a2 > b2:
    (a2, b2) = (b2, a2)
if b2 > c2:
    (b2, c2) = (c2, b2)
    if a2 > b2:
        (a2, b2) = (b2, a2)

if a1 == a2 and b1 == b2 and c1 == c2:
    r = 'Boxes are equal'
elif a1 <= a2 and b1 <= b2 and c1 <= c2:
    r = 'The first box is smaller than the second one'
elif a2 <= a1 and b2 <= b1 and c2 <= c1:
    r = 'The first box is larger than the second one'
else:
    r = 'Boxes are incomparable'
print(r)

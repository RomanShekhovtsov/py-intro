# 7_04 meet_before
lst = map(int, input().split())
s = set()

for n in lst:
    if n in s:
        print('YES')
    else:
        print('NO')
        s.add(n)

# 5_05 flags
n = int(input())
flag = (
    '+___ ',
    '|X / ',
    '|__\ ',
    '|    ')

for s in flag:
    for i in range(n):
        if s == flag[1]:
            print(s[0], i + 1, s[2:], sep='', end='')
        else:
            print(s, end='')
    print()

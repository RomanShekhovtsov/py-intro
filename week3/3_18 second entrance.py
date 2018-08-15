# 3_18 second entrance
s = input()
first = s.find('f')
if first == -1:
    print(-2)
else:
    last = s[first + 1:].find('f')
    if last == -1:
        print(-1)
    else:
        print(first + last + 1)

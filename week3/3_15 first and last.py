# 3_15 first and last
s = input()
first = s.find('f')
last = s[::-1].find('f')
# print(first, last)
if first > -1:
    print(first, end='')
if last > -1:
    last = len(s) - last - 1
    if last != first:
        print(' ' + str(last))

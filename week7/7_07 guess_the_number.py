# 7_07 guess_the_number
DEBUG = False


def read_line(f):
    if f is None:
        s = input()
    else:
        s = f.readline()
    return s.strip()

if DEBUG:
    f = open('tests/7_07_4.txt', 'r', encoding='utf-8')
else:
    f = None

n = int(read_line(f))
may_be = set(range(1, n + 1))

lst = []
s = ''
while s != 'HELP':
    s = read_line(f)
    lst.append(s)

for i in range(0, len(lst) - 1, 2):
        nums = set(map(int, lst[i].split()))
        if lst[i + 1] == 'YES':
            may_be &= nums
        else:
            may_be -= nums

if DEBUG:
    f.close()

print(*sorted(may_be))

# 7_09 polyglots
DEBUG = False
tests = [1]


def read_file(filename):
    f = open(filename, 'r', encoding='utf-8')
    s = f.read()
    f.close()
    return s


def print_list(A, sep=' ', end='\n'):
    for x in A:
        print(x, end=sep)
    print(end, end='')


def read_line(f):
    if f is None:
        s = input()
    else:
        s = f.readline()
    return s.strip()

if DEBUG:
    f = open('tests/7_09_1.txt', 'r', encoding='utf-8')
else:
    f = None

know_all = None
all_langs = set()

n = int(read_line(f))
for i in range(n):
    m = int(read_line(f))
    langs = set()
    for j in range(m):
        langs.add(read_line(f))

    if know_all is None:
        know_all = langs
    else:
        know_all &= langs
    all_langs |= langs

if DEBUG:
    f.close()

print(len(know_all))
print_list(know_all, '\n', end='')
print(len(all_langs))
print_list(all_langs, '\n')

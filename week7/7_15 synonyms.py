# 7_15 synonyms
DEBUG = False
tests = [1, 2, 3]


def read_file(filename):
    f = open(filename, 'r', encoding='utf-8')
    s = f.read()
    f.close()
    return s.strip()


def synonyms(s):
    lst = s.split('\n')
    dic = {}
    n = int(lst[0])
    for s in lst[1:-1]:
        syns = s.split()
        dic[syns[0]] = syns[1]
        dic[syns[1]] = syns[0]
    print(dic[lst[-1]])

if DEBUG:
    for t in tests:
        s = read_file('tests/7_15_' + str(t) + '.txt')
        synonyms(s)
else:
    s = read_file('input.txt')
    synonyms(s)

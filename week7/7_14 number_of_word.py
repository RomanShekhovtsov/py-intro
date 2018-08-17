# 7_14 number_of_word
DEBUG = False
tests = [1, 2, 3]


def read_file(filename):
    f = open(filename, 'r', encoding='utf-8')
    s = f.read()
    f.close()
    return s.strip()


def number_of_word(s):
    lst = s.split()
    dic = {}
    for w in lst:
        print(dic.get(w, 0), end=' ')
        dic[w] = dic.get(w, 0) + 1

if DEBUG:
    for t in tests:
        s = read_file('tests/7_14_' + str(t) + '.txt')
        number_of_word(s)
        print()
else:
    s = read_file('input.txt')
    number_of_word(s)

# 7_06 words_count
fname = 'input.txt'


def read_file(filename):
    inf = open(filename, 'r', encoding='utf-8')
    s = inf.read()
    inf.close()
    return s

lst = read_file(fname).split()
print(len(set(lst)))

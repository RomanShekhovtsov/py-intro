# 7_01 count_of_numbers
tests = [1, 2, 3]


def read_file(filename):
    inf = open(filename, 'r', encoding='utf-8')
    s = inf.read()
    inf.close()
    return s

# for t in tests:
#    lst = read_file('tests/7_01_' + str(t) + '.txt').split()
#    print(len(set(lst)))
lst = input().split()
print(len(set(lst)))

# 7_03 intersection
tests = [1, 2]


def read_file(filename):
    inf = open(filename, 'r', encoding='utf-8')
    s = inf.read()
    inf.close()
    return s


def print_list(A, sep=' '):
    for x in A:
        print(x, end=sep)
    print()

# for t in tests:
#    lst = read_file('tests/7_02_' + str(t) + '.txt').split('\n')
#    a = set(lst[0].split())
#    b = set(lst[1].split())
#    print(a & b)

a = set(map(int, input().split()))
b = set(map(int, input().split()))
print_list(sorted(a & b))

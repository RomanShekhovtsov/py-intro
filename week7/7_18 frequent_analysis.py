# 7_18 frequent_analysis
DEBUG = False
tests = [1, 2, 3]


def read_file(filename):
    f = open(filename, 'r', encoding='utf-8')
    s = f.read()
    f.close()
    return s.strip()


def print_list(A, sep=' ', end='\n'):
    for x in A:
        print(x, end=sep)
    print(end, end='')


def frequent_analysis(s):
    text = s.split()
    words = {}
    for word in text:
        words[word] = words.get(word, 0) + 1
    for word in sorted(words.items(), key=lambda x: (-x[1], x[0])):
        print(word[0])

if DEBUG:
    for t in tests:
        s = read_file('tests/7_18_' + str(t) + '.txt')
        frequent_analysis(s)
        print()
else:
    s = read_file('input.txt')
    frequent_analysis(s)

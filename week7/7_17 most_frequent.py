# 7_17 most_frequent
DEBUG = False
tests = [1, 2, 3]


def read_file(filename):
    f = open(filename, 'r', encoding='utf-8')
    s = f.read()
    f.close()
    return s.strip()


def most_frequent(s):
    text = s.split()
    words = {}
    for word in text:
        words[word] = words.get(word, 0) + 1
    print(sorted(words.items(), key=lambda x: (-x[1], x[0]))[0][0])

if DEBUG:
    for t in tests:
        s = read_file('tests/7_17_' + str(t) + '.txt')
        most_frequent(s)
else:
    s = read_file('input.txt')
    most_frequent(s)

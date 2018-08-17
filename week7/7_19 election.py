# 7_19 election
DEBUG = False
tests = [1, 2]


def read_file(filename):
    f = open(filename, 'r', encoding='utf-8')
    s = f.read()
    f.close()
    return s.strip()


def save_file(filename, data):
    f = open(filename, 'w', encoding='utf8')
    print(data, file=f)
    f.close


def election(s):
    text = s.split('\n')
    total = 0
    names = {}
    for name in text:
        names[name] = names.get(name, 0) + 1
        total += 1

    sorted_names = sorted(names.items(), key=lambda x: -x[1])
    if sorted_names[0][1] > total / 2:
        return sorted_names[0][0]
    else:
        return sorted_names[0][0] + '\n' + sorted_names[1][0]

if DEBUG:
    for t in tests:
        s = read_file('tests/7_19_' + str(t) + '.txt')
        print(election(s))
else:
    s = read_file('input.txt')
    save_file('output.txt', election(s))

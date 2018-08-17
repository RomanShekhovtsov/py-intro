# 6_14 pass_score
tests = [1, 2, 3]


def read_file(filename):
    inf = open(filename, 'r', encoding='utf-8')
    s = inf.read()
    inf.close()
    return s


def save_file(filename, data):
    f = open(filename, 'w', encoding='utf8')
    print(data, file=f)
    f.close


def pass_score(lst):
    k = int(lst[0])
    scores = []
    for i in range(1, len(lst)):
        line_list = lst[i].split()
        if len(line_list) == 0:
            continue

        ex1, ex2, ex3 = line_list[-3:]
        ex1, ex2, ex3 = int(ex1), int(ex2), int(ex3)
        if min((ex1, ex2, ex3)) >= 40:
            sum = ex1 + ex2 + ex3
            scores.append(sum)
    scores.sort(reverse=True)

    if k >= len(scores):
        return 0
    else:
        if scores[k] == max(scores):
            return 1
        else:
            for i in range(k, 0, -1):
                if scores[i - 1] != scores[i]:
                    return scores[i - 1]
            return scores[0]

# for t in tests:
#    data = read_file('tests/6_14_' + str(t) + '.txt').split('\n')
#    print(pass_score(data))
#    print()

data = read_file('input.txt').split('\n')
res = pass_score(data)
save_file('output.txt', res)

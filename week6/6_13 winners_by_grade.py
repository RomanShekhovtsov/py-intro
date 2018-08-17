# 6_13 winners_by_grade
tests = [1, 2, 3]


def read_file(filename):
    f = open(filename, 'r', encoding='utf8')
    s = f.read()
    f.close()
    return s


def save_file(filename, data):
    f = open(filename, 'w', encoding='utf8')
    print(data, file=f)
    f.close


class Winners:
    count = 0
    max_score = 0


def winners_by_grade(lst):
    winners = [Winners(), Winners(), Winners()]
    min_grade = 9
    for line in lst:
        if len(line) == 0:
            continue

        surname, name, grade, score = line.split()
        grade = int(grade)
        score = int(score)

        winner = winners[grade - min_grade]

        if score == winner.max_score:
            winner.count += 1

        if score > winner.max_score:
            winner.count = 1
            winner.max_score = score

    res = []
    for w in winners:
        res.append(w.count)
    return res

# for t in tests:
#     data = read_file('tests/6_13_' + str(t) + '.txt').split('\n')
#     print_list(winners_by_grade(data))

data = read_file('input.txt').split('\n')
res = winners_by_grade(data)
save_file('output.txt', ' '.join(map(str, res)))

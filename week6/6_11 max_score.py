# 6_11 max_score
# data = readtest(6, 11, 1)


def read_file(filename):
    f = open(filename, 'r', encoding='utf-8-sig')
    s = f.read()
    f.close()
    return s


def save_file(filename, data):
    f = open(filename, 'w', encoding='utf-8')
    print(data, file=f)
    f.close


def print_list(A, sep=' '):
    for x in A:
        print(x, end=sep)
    print()


def max_score(s):
    min_grade = 9
    max_points = [0] * 3

    for line in s.split('\n'):
        if len(line) == 0:
            continue
        surname, name, grade, point = line.split()
        grade = int(grade)
        point = int(point)
        max_point = max_points[grade - min_grade]
        if point > max_point:
            max_points[grade - min_grade] = point
    return max_points

data = read_file('input.txt')
res = max_score(data)
save_file('output.txt', ' '.join(map(str, res)))

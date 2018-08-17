# 6_08 sort_by_name
tests = [1, 2, 3]


class Participant:
    surname = ''
    name = ''
    point = ''


def sort_by_name(filename):
    lst = []

    inf = open(filename, 'r', encoding='utf-8')
    for line in inf:
        p = Participant()
        p.surname, p.name, grade, p.point = line.split()
        lst.append(p)
    inf.close

    lst.sort(key=lambda x: x.surname)

    for p in lst:
        print(p.surname, p.name, p.point)

# for t in tests:
#     sort_by_name("tests/6_08_" + str(t) + ".txt")
#     print()

sort_by_name("input.txt")

# 6_07 grade_point_average
test_files = ['6_07_1.txt', '6_07_2.txt', '6_07_3.txt']


class Grade:
    sum_points = 0
    count = 0


def grade_point_average(filename):
    min_grade = 9
    grades = [Grade(), Grade(), Grade()]

    inf = open(filename, 'r', encoding='utf-8')
    for line in inf:
        surname, name, grade, point = line.split()
        grade = int(grade)
        point = int(point)
        g = grades[grade - min_grade]
        g.sum_points = g.sum_points + point
        g.count = g.count + 1
    inf.close

    for g in grades:
        print(g.sum_points / g.count, end=' ')
    print()

# for f in test_files:
#    grade_point_average(f)

grade_point_average('input.txt')

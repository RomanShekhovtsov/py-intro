# 6_09 sort_by_counting
tests = [1, 2, 3]


def CountSort(A):
    k = max(A) + 1
    C = [0] * k

    for a in A:
        C[a] = C[a] + 1

    b = 0
    for j in range(0, k):
        for i in range(0, C[j]):
            A[b] = j
            b = b + 1
    return A


def readtest(week_num, exercise_num, test_num):
    filename = "tests/" + str(week_num) + "_" + \
        '{:02d}'.format(exercise_num) + "_" + str(test_num) + ".txt"
    inf = open(filename, 'r', encoding='utf-8')
    s = inf.read()
    inf.close()
    return s


def print_list(A):
    for x in A:
        print(x, end=' ')
    print()

# for t in tests:
#     s = readtest(6, 9, t)
#     res = CountSort(list(map(int, s.split())))
#     print_list( res )

s = input()
res = CountSort(list(map(int, s.split())))
print_list(res)

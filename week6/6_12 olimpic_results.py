# 6_12 olimpic_results
tests = [1, 2, 3]


def olimpic_results(lst):
    res = lst[1:]
    res.sort(key=lambda x: -int(x.split()[1]))

    for x in res:
        print(x.split()[0])

# for t in tests:
#    data = readtest(6, 12, t).split('\n')
#    olimpic_results(data)

n = input()
data = [n]
for i in range(int(n)):
    data.append(input())
olimpic_results(data)

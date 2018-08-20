# 9_02 add_multiply
from sys import stdin


class Matrix:

    def __init__(self, lists):
        self.lists = []
        for list in lists:
            self.lists.append(list[:])

    def __str__(self):
        res = []
        for list in self.lists:
            res.append('\t'.join(map(str, list)))
        return '\n'.join(res)

    def __add__(self, m2):
        res = Matrix(m2.lists)
        for i in range(0, len(self.lists)):
            for j in range(0, len(self.lists[0])):
                res.lists[i][j] += self.lists[i][j]
        return res

    def __mul__(self, n):
        res = Matrix(self.lists)
        for i in range(0, len(self.lists)):
            for j in range(0, len(self.lists[0])):
                res.lists[i][j] *= n
        return res

    __rmul__ = __mul__

    def size(self):
        return(len(self.lists), len(self.lists[0]))

# m = Matrix([
#    [0, 1, 2],
#    [1, 0, 1],
#    [3, 1, 0]])
#
# m2 = Matrix([
#    [0, 1, 2],
#    [1, 0, 1],
#    [3, 1, 0]])
# print(m + m2)
# print(m * 8)

exec(stdin.read())

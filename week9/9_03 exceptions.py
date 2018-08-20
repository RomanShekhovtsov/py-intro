# 9_03 exceptions
from sys import stdin


class MatrixError(BaseException):

    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


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
        if len(m2.lists) != len(self.lists):
            raise MatrixError(self, m2)

        if len(m2.lists[0]) != len(self.lists[0]):
            raise MatrixError(self, m2)

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

    def transpose(self):
        self.lists = Matrix.transposed(self).lists
        return self

    @staticmethod
    def transposed(m):
        res = []
        for i in range(len(m.lists[0])):
            res.append([])
            for j in range(len(m.lists)):
                res[i].append(m.lists[j][i])
        return Matrix(res)

# m = Matrix([
#    [0, 1],
#    [1, 0]])
# m2 = Matrix([
#    [0, 1],
#    [2, 3],
#    [4, 5]])
# try:
#    print(m2)
#    print()
#    m3 = m2.transpose()
#    print(m2)
#    print()
#    print(m3)
#    print()
#    print(Matrix.transposed(m2))
# except MatrixError as me:
#    print(me.matrix1)
#    print(me.matrix2)

exec(stdin.read())

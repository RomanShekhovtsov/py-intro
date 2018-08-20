# 9_01 class
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

    def size(self):
        return(len(self.lists), len(self.lists[0]))

# m = Matrix([
#    [0, 1, 2],
#    [1, 0, 1],
#    [3, 1, 0]])
# print(m)
# print(m.size())
exec(stdin.read())

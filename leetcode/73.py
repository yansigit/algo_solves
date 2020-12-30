from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    table = dict()
    for i, v in enumerate(matrix):
        if 0 in v:
            for index, value in enumerate(v):
                if value == 0:
                    table[index] = 1
            matrix[i] = [0] * len(matrix[i])
    for i, v in enumerate(matrix):
        for index, value in enumerate(v):
            if index in table.keys() and table[index] == 1:
                matrix[i][index] = 0
    print(matrix)


setZeroes(matrix=[[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]])

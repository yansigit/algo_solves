from typing import List


def rotate(matrix: List[List[int]]) -> None:
    matrix.reverse()
    for i in range(len(matrix)):
        for j in range(len(matrix[i][i+1:])):
            matrix[-1*(j+1)][i], matrix[i][-1*(j+1)] = matrix[i][-1*(j+1)], matrix[-1*(j+1)][i]
    print(matrix)


rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
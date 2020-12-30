from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result: List[int] = []
    while len(matrix) > 0:
        try:
            result.extend(matrix.pop(0))
            for i in range(len(matrix)):
                result.append(matrix[i].pop(-1))
            result.extend(reversed(matrix.pop(-1)))
            # 역순
            for i in range(len(matrix)-1, -1, -1):
                result.append(matrix[i].pop(0))
            # print(result, matrix)
        except IndexError:
            break
    return result


spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]])

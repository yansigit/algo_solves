# N = int(input())
# 한 블록씩 출력?
# 픽셀 처리를 어떻게 해야하나?
# 벡터?
from copy import deepcopy

N = int(input())

_vector = ["*"] * N
_vector = [deepcopy(_vector)] * N

def testThing(N) -> []:
    _t = N // 3
    global _vector
    for i in range(_t, _t + _t):
        for j in range(_t, _t + _t):
            _vector[i][j] = ' '

testThing(N)

print(_vector)
print("done")
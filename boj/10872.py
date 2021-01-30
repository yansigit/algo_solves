N = int(input())

def test(N, rst):
    if N <= 1:
        return rst
    rst = N * rst
    tt = test(N-1, rst)
    return tt

print(test(N, 1))
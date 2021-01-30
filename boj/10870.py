N = int(input())


def test(N):
    if N == 0:
        return 0
    if N == 1:
        return 1
    return test(N - 1) + test(N - 2)


print(test(N))

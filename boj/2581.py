from math import sqrt

M, N = int(input()), int(input())

# table = defaultdict(lambda: True)
table = [True] * (N+1)
table[0], table[1] = False, False
for i in range(2, int(sqrt(N)) + 1):
    if table[i]:
        j = 2
        while i*j <= N:
            table[i*j] = False
            j += 1
rtn = [i for i, a in enumerate(table) if a and i >= M]
if len(rtn) > 0:
    print(sum(rtn))
    print(rtn[0])
else:
    print(-1)
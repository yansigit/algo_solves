N, M = map(int, input().split())
out = []

def solve(idx, N, M):
    if len(out) == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        out.append(i+1)
        solve(i, N, M)
        out.pop()

solve(0, N, M)
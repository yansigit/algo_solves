N, M = map(int, input().split())
visited = [False] * N
out = []


def solve(idx, N, M):
    if len(out) == M:
        print(' '.join(map(str, out)))
        return
    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            out.append(i + 1)
            solve(i + 1, N, M)
            visited[i] = False
            out.pop()


solve(0, N, M)

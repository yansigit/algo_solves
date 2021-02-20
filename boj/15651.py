n, m = map(int, input().split())

check = [False for i in range(n + 1)]
subs = []


def go(n, m):
    if len(subs) == m and subs:
        print(' '.join(map(str, subs)))
        return

    for i in range(1, n + 1):
        check[i] = True
        subs.append(i)
        go(n, m)
        check[i] = False
        subs.pop()


go(n, m)

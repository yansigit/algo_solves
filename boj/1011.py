T = int(input())

for _ in range(T):
    start,end = map(int, input().split())
    if end - start <= 3:
        print(end-start)

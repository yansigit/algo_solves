N = int(input())

cnt = 1
range_s, range_end = 1, 1

if N == 1:
    print(cnt)
else:
    while True:
        range_s = range_end + 1
        range_end = range_end + (6 * cnt)
        if range_s <= N <= range_end:
            print(cnt+1)
            break
        cnt += 1

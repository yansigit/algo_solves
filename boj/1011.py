case_num = int(input())
for i in range(case_num):
    a, b = map(int, input().split())
    num = b-a
    k = 1
    p = 1
    while num > 0:
        num -= k
        k += 1
        if num >= p:
            num -= p
            p += 1

    print(k+p-2)
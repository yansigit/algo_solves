from math import sqrt

a, b = map(int, input().split())
table = [True] * (b+1)
table[0], table[1] = False, False

for i in range(2, int(sqrt(b)) + 1):
    if table[i]:
        j = 2
        while i*j <= b:
            table[i*j] = False
            j += 1
for i in (i for i, ele in enumerate(table) if i >= a and ele):
    print(i)
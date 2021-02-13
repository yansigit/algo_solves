N = int(input())

count = 0
for i in range(666, 10000666):
    if str(i).count('666') < 1:
        continue
    count += 1
    if count == N:
        print(i)
        break

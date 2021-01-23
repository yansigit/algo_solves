# 1/1
# 1/2, 2/1
# 3/1, 2/2, 1/3
# 4/1, 3/2, 2/3, 1/4

# 1
# 2~3
# 4~6
# 7~10

X = int(input())

start, end = 0, 0
i = 0
while True:
    if X == 1:
        break
    start = end + 1
    end = start + i
    if start <= X <= end:
        break
    i += 1


# 몇번째 수 집합, 집합의 몇번째 인덱스
# print(i + 1, X - start)
# 몇번째 집합인지에 따라 배열 생성
arr = list(range(1, (i + 1) + 1))

rtn = ""
if X == 1:
    print("1/1")
else:
    if (i+1) % 2 == 0:
        rtn = str(arr[X - start]) + "/" + str(arr[-1 * ((X - start) + 1)])
    else:
        rtn = str(arr[-1 * ((X - start) + 1)]) + "/" + str(arr[X - start])

print(rtn)

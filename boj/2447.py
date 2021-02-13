n = int(input())  # input
arr = [["*"] * n for _ in range(n)]  # output array 생성

v = n
cnt = 0
while v != 1:  # 입력받은 n이 3의 몇승?
    v /= 3
    cnt += 1

for cnt_ in range(cnt):
    idx = [i for i in range(n) if (i // 3 ** cnt_) % 3 == 1]  # 빈칸으로 채울 행/열 index
    for i in idx:
        for j in idx:
            arr[i][j] = " "

# 출력
print('\n'.join([''.join([str(i) for i in row]) for row in arr]))

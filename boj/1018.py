w, h = map(int, input().split())
diff_w, diff_h = w-7, h-7
arr = []
for _ in range(w):
    arr.append(str(input()))

# 0~9
# 0~7, 1~8, 2~9
rst_arr = []
for i in range(diff_w):
    for j in range(diff_h):
        cnt = 0
        cnt2 = 0
        for x in range(i, i+8, 2):
            for z in range(j, j+8):
                for t in range(1):
                    if (z-j) % 2 == 0:
                        if arr[x][z] != "W":
                            cnt += 1
                        if arr[x+1][z] != "B":
                            cnt += 1
                    else:
                        if arr[x][z] != "B":
                            cnt += 1
                        if arr[x+1][z] != "W":
                            cnt += 1
                    if (z-j) % 2 == 1:
                        if arr[x][z] != "W":
                            cnt2 += 1
                        if arr[x+1][z] != "B":
                            cnt2 += 1
                    else:
                        if arr[x][z] != "B":
                            cnt2 += 1
                        if arr[x+1][z] != "W":
                            cnt2 += 1
        rst_arr.append(cnt)
        rst_arr.append(cnt2)

print(min(rst_arr))
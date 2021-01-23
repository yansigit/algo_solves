lp = int(input())
for _ in range(lp):
    footprint = 0
    H, W, N = [int(a) for a in input().split(" ")]
    YY = N % H
    XX = N // H + 1
    if YY == 0:
        YY = H
        XX -= 1
    if XX < 10:
        XX = "0" + str(XX)
    print(str(YY) + str(XX))


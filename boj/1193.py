# 1/1 -> 2 --> 1
# 1/2 2/1 -> 3 --> 2,3
# 3/1 2/2 1/3 -> 4 --> 4,5,6
# 1/4 2/3 3/2 4/1 -> 5 --> 7,8,9,10
# 5/1 4/2 3/3 2/4 1/5 -> 6  --> 11,12,13,14,15

cnt = 1
range_s, range_r, range_end = 1, 1, 1

while 1:
    range_s = range_end + 1
    range_e = range_s + range_r
    range_r += 1



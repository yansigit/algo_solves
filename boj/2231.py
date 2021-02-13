number = input()
limit = len(number) * 9

rst_arr = []
if limit > int(number):
    _temp = int(number) - limit
for i in range(limit, int(number)):
    num_arr = list(str(i))
    num_arr = list(map(int, num_arr))
    # print(i, num_arr, i + sum(num_arr))
    # print(i + sum(num_arr))
    if int(number) == i + sum(num_arr):
        rst_arr.append(i)

if len(rst_arr) > 0:
    print(rst_arr[0])
else:
    print(0)
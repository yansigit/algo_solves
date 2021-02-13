input_count = int(input())
inputs = []
for _ in range(input_count):
    inputs.append(tuple(map(int, input().split())))

for i in inputs:
    rank = 1
    for j in inputs:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")

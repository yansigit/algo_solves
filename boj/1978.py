import math


def is_prime_number(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


_ = input()
arr = [int(a) for a in input().split()]
cnt = 0
for a in arr:
    if is_prime_number(a):
        cnt += 1
print(cnt)

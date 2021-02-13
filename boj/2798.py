card_count, max_number = map(int, input().split())
cards = list(map(int, input().split()))

cnt = 0
_max = 0
_sum = 0
for i in range(card_count):
    for j in range(card_count):
        if j == i: continue
        for k in range(card_count):
            if k == j or k == i: continue
            _sum = cards[i] + cards[j] + cards[k]
            if max_number >= _sum > _max:
                _max = _sum

print(_max)

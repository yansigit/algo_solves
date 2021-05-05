buttons = {1: [0, 0], 2: [0, 1], 3: [0, 2], 4: [1, 0], 5: [1, 1], 6: [1, 2], 7: [2, 0], 8: [2, 1], 9: [2, 2],
           0: [3, 1]}

l_currentPosition = [3, 0]
r_currentPosition = [3, 2]
result = ""
_hand = "right"


def pressButton(num):
    global result, l_currentPosition, r_currentPosition, _hand, buttons
    if num == 1 or num == 4 or num == 7:
        result += "L"
        l_currentPosition = buttons[num]
    elif num == 3 or num == 6 or num == 9:
        result += "R"
        r_currentPosition = buttons[num]
    else:
        left_move = abs(buttons[num][0] - l_currentPosition[0]) + abs(buttons[num][1] - l_currentPosition[1])
        right_move = abs(buttons[num][0] - r_currentPosition[0]) + abs(buttons[num][1] - r_currentPosition[1])
        if left_move < right_move:
            result += "L"
            l_currentPosition = buttons[num]
        elif right_move < left_move:
            result += "R"
            r_currentPosition = buttons[num]
        elif right_move == left_move:
            if _hand == "right":
                result += "R"
                r_currentPosition = buttons[num]
            elif _hand == "left":
                result += "L"
                l_currentPosition = buttons[num]


def solution(numbers, hand):
    global result, _hand
    _hand = hand
    for a in numbers:
        pressButton(a)
    return result

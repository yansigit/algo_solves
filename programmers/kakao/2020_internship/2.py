from copy import copy
from itertools import permutations
import re

re_num = re.compile(r"(\d+)")
re_sym = re.compile(r"[-*+]")


def solution(expression):
    nums = re_num.findall(expression)
    nums = [int(a) for a in nums]
    syms = re_sym.findall(expression)
    biggest = -9999999999999

    for order in (list(permutations(set(syms)))):
        # print("경우:", order)
        # print("연산:", nums, syms)

        _nums = copy(nums)
        _syms = copy(syms)

        # 각 경우의 기호마다 연산
        # 예 = order = (*, -, +)
        for sym in order:
            while sym in _syms:
                i = _syms.index(sym)
                if sym == '+':
                    _nums[i] = _nums[i] + _nums[i+1]
                    # _nums.pop(i+1)
                    # _syms.pop(i)
                elif sym == '-':
                    _nums[i] = _nums[i] - _nums[i + 1]
                elif sym == '*':
                    _nums[i] = _nums[i] * _nums[i + 1]
                _nums.pop(i + 1)
                _syms.pop(i)
                # print(_nums, _syms)

        _nums[0] = abs(_nums[0])
        if _nums[0] > biggest:
            biggest = _nums[0]

    return biggest

print("답: ", solution("100-200*300-500+20"))
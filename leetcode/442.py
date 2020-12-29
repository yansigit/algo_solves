from typing import List


def findDuplicates(nums: List[int]) -> List[int]:
    table = dict()
    for num in nums:
        if num in table.keys():
            table[num] += 1
            continue
        table[num] = 1
    print(table)
    return [k for k, v in table.items() if v > 1]

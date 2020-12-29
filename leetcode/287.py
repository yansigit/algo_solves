from typing import List


def findDuplicate(nums: List[int]) -> int:
    table = set()
    for num in nums:
        if num in table:
            return num
        table.add(num)


print(findDuplicate([1, 2, 3, 4, 5, 5, 6, 7, 8]))

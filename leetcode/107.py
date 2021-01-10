# Definition for a binary tree node.
from collections import deque
from copy import copy


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode):
        if not root:
            return []

        queue = deque([root])
        result = []

        while queue:
            result.append([node.val for node in queue])
            for node in copy(queue):
                for child in (node.left, node.right):
                    if node:
                        queue.append(child)
                queue.popleft()

        return reversed(result)
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        queue = ([root])
        rtn = []

        i = 1
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                tmp.append(node.val)
            if i % 2 == 0:
                tmp.reverse()
            rtn.append(tmp)
            i += 1

        return rtn
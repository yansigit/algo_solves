class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = [root]

        while queue:
            for _ in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            for i in range(len(queue)-1):
                if queue[i+1]:
                    queue[i].next = queue[i+1]

        return root
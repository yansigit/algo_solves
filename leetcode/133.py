class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        queue = deque([node])
        table = {node.val:Node(node.val)}

        while queue:
            _node = queue.pop()
            for neighbor in _node.neighbors:
                if neighbor.val not in table:
                    table[neighbor.val] = Node(neighbor.val)
                    queue.appendleft(neighbor)
                table[_node.val].neighbors.append(table[neighbor.val])

        return table[node.val]
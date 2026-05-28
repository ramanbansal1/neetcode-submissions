from collections import deque

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # original -> clone
        clones = {}

        # create clone for starting node
        clones[node] = Node(node.val)

        q = deque([node])

        while q:
            curr = q.popleft()

            for neighbor in curr.neighbors:

                # if neighbor not cloned yet
                if neighbor not in clones:
                    clones[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                # connect cloned nodes
                clones[curr].neighbors.append(clones[neighbor])

        return clones[node]
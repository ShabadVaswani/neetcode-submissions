"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        visited = {}
        adjlist = []

        def dfs(currnode):
            if currnode in visited:
                return visited[currnode]
            newNode = Node(currnode.val)
            visited[currnode] = newNode
            for neighbour in currnode.neighbors:
                if neighbour in visited:
                    newNode.neighbors.append(visited[neighbour])
                else:
                    newNode.neighbors.append(dfs(neighbour))

            return newNode
            

        return dfs(node)

        
        
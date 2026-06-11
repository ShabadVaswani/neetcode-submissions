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

        def dfs(curr):
            adjlist = []
            if curr in visited:
                return visited[curr]
            newNode = Node(curr.val)
            visited[curr] = newNode
            for n in curr.neighbors:
                adjlist.append(dfs(n))
            newNode.neighbors = adjlist
            return newNode
        

        return dfs(node)
        
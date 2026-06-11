class Node:
    def __init__(self, val = 0, adj = None):
        self.val = val
        self.adj = adj

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if edges == []:
            return True
        nodedict = {}
        visited = set()
        self.flag = True
        for p, c in edges:
            if c not in nodedict:
                nodedict[c] = Node(c, [])
            if p not in nodedict:
                nodedict[p] = Node(p, [nodedict[c]])
                nodedict[c].adj.append(nodedict[p])
            else:
                nodedict[p].adj.append(nodedict[c])
                nodedict[c].adj.append(nodedict[p])


        def dfs(root,pre):
            print(root.val)
            if root.val in visited:
                self.flag = False
                return []
            visited.add(root.val)
            if root.adj == []:
                return [root.val]
            res = []
            for child in root.adj:
                if child.val == pre:
                    continue
                res.extend(dfs(child, root.val))
            res.append(root.val)
            return res
        
        dfs(nodedict[0],-1)
        return len(visited) == n if self.flag else False




            
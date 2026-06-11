class ListNode:
    def __init__(self, val = 0, adjlist = []):
        self.val = val
        self.adjlist = adjlist

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        nodedict = {}
        self.visiting = set()
        self.visited = set()
        for c,p in prerequisites:
            if p not in nodedict:
                nodedict[p] = ListNode(p, [])
            if c not in nodedict:
                nodedict[c] = ListNode(c, [nodedict[p]])
            else:
                nodedict[c].adjlist.append(nodedict[p])
        def dfs(i, visiting):
            if i in self.visited:
                return True
            if i in visiting:
                for x in visiting:
                    print(x.val)
                return False
            visiting.add(i)
            for i in i.adjlist:
                if not dfs(i, visiting.copy()):
                    return False
            return True
                
        for i in range(numCourses):
            if i in nodedict:
                if not dfs(nodedict[i], set()):
                    return False
                self.visited.add(nodedict[i])
            self.visiting = set()
                    
        return True



        
            
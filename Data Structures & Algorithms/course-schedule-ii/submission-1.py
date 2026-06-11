class ListNode:
    def __init__(self, val = 0, adj = None):
        self.val = val
        self.adj = adj
        self.inwardct = 0
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        nodedict = {}
        visited = set()
        q = deque()
        count = numCourses
        res = []
        for p, c in prerequisites:
            if p not in nodedict:
                nodedict[p] = ListNode(p, [])
            if c not in nodedict:
                nodedict[c] = ListNode(c, [nodedict[p]])
            else:
                nodedict[c].adj.append(nodedict[p])
            nodedict[p].inwardct+=1

        for i in range(numCourses):
            if i in nodedict:
                if nodedict[i].inwardct == 0:
                    q.append(nodedict[i])
                    count-=1
            else:
                nodedict[i] = ListNode(i, [])
                q.append(nodedict[i])
                count-=1

        while q:
            curr = q.popleft()
            val, adj = curr.val, curr.adj
            res.append(val)
            if adj == None:
                continue
            for i in curr.adj:
                print(i)
                i.inwardct -=1
                if i.inwardct == 0:
                    q.append(i)
                    count-=1
        if count == 0:
            return res
        return []
            














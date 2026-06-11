class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        premap = {i:[] for i in range(numCourses)}

        for cr, pre in prerequisites:
            premap[cr].append(pre)


        visited = set()

        def dfs(cr):
            if cr in visited:
                return False

            if premap[cr] == []:
                return True

            visited.add(cr)
            for i in premap[cr]:
                if not dfs(i): return False
            visited.remove(cr)
            premap[cr] = []

            return True

        for cr in range(numCourses):
            if not dfs(cr):
                return False
        return True
            
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        mem = {}
        def dfs(i, j):
            if i not in range(m) or j not in range(n):
                return 0
            if i == m-1 and j == n-1:
                return 1
            if (i, j) in mem:
                return mem[(i,j)]
            totalpaths = 0
            rightpaths = dfs(i + 1, j)
            leftpaths = dfs(i, j + 1)

            if rightpaths != 0:
                totalpaths += rightpaths

            if leftpaths != 0:
                totalpaths += leftpaths
            mem[(i,j)] = totalpaths
            return totalpaths

        return dfs(0, 0)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        mem = {}

        def dfs(i,j):
            res = 0
            if (i,j) in mem:
                return mem[(i,j)]
            if i == len(s):
                if j == len(t):
                    return 1
                else:
                    return 0
            if j == len(t):
                return 1
            if s[i] == t[j]:
                res+=dfs(i+1,j+1)
                res+=dfs(i+1,j)
            else:
                res+=dfs(i+1,j)
            mem[(i,j)] = res
            return res
        return dfs(0,0)
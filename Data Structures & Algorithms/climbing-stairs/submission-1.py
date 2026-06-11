class Solution:
    def climbStairs(self, n: int) -> int:
        
        stepmem = collections.defaultdict()
        def dfs(curr):
            if curr == n:
                return 1
            if curr > n:
                return 0
            if curr in stepmem:
                return stepmem[curr]
            onect = dfs(curr+1)
            twoct = dfs(curr+2)
            stepmem[curr] = onect+twoct
            return onect + twoct

        return dfs(0)
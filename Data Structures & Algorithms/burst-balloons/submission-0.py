class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        newList = [1] + nums + [1]
        mem = {}
        def dfs(l, r):
            if l > r:
                return 0
            if (l,r) in mem:
                return mem[(l,r)]
            mem[(l,r)] = 0
            for i in range(l, r+1):
                curr = newList[l-1] * newList[i] * newList[r+1]
                curr+= dfs(l, i-1) + dfs(i+1, r)
                mem[(l,r)] = max(mem[(l,r)], curr)
            return mem[(l,r)]
        
        return dfs(1, len(newList)-2)
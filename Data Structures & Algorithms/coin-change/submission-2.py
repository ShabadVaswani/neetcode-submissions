class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        mem = {}
        def dfs(currsum):
            if currsum in mem:
                return mem[currsum]
            reqd = amount - currsum
            if reqd==0:
                return 0
            res = float('inf')
            
            for  coin in coins:
                if coin > reqd:
                    break
                count = 0
                count +=dfs(currsum+coin)+1
                res=min(res, count)
                
            mem[currsum] = res
            return res
        result = dfs(0)
        return result if result < 2*amount else -1
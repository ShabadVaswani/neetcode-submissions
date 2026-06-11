class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mem = {}

        def dfs(i, buying):
            if i > len(prices)-1:
                return 0

            if (i, buying) in mem:
                return mem[(i,buying)]

            if buying:
                buy = dfs(i+1, False) - prices[i]
                cooldown = dfs(i+1, True)
                mem[i, buying] = max(cooldown, buy)
                return mem[i, buying] 

            if not buying:
                sell = dfs(i+2, True) + prices[i]
                cooldown = dfs(i+1, False)
                mem[i, buying] = max(cooldown, sell)
                return mem[i, buying] 

        return dfs(0, True)
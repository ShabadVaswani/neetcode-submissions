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
                return max(cooldown, buy)

            if not buying:
                sell = dfs(i+2, True) + prices[i]
                cooldown = dfs(i+1, False)
                return max(cooldown, sell)

        return dfs(0, True)
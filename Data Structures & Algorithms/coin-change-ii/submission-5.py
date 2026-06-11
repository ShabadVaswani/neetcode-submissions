class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        mem = {}
        coins.sort()

        def dfs(index, cursum):
            if (index, cursum) in mem:
                return mem[(index, cursum)]
            if index > len(coins)-1:
                return 0 

            temp = coins[index] + cursum
            if temp == amount:
                return 1
            if temp > amount:
                return 0
            paths = 0
            paths+=dfs(index, cursum+coins[index])
            paths+=dfs(index+1, cursum)
            mem[(index, cursum)] = paths
            return paths

        return dfs(0, 0)
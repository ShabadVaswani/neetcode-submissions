class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        stepmem = {}
        def dfs(step):
            if step in stepmem:
                return stepmem[step]
            if step == n:
                return 1
            if step == n-1 or step == n-2:
                return cost[step]
            print(step, n)
            stepmem[step] = cost[step] + min(dfs(step+1), dfs(step+2))
            return stepmem[step]

        return min(dfs(0), dfs(1))
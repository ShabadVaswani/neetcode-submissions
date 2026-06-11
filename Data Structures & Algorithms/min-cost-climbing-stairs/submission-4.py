class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        c1, c2 = cost[-2], cost[-1]
        for i in range(n-3, -1, -1):
            
            c2, c1 = c1, cost[i] + min(c1, c2)

            print(i, c1, c2)

        print(c1, c2)
        return min(c1, c2)

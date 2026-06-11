class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        housemem = {}
        def dfs(house):
            if house in housemem:
                return housemem[house]
            if house == n:
                return 0
            if house == n-1 or house == n-2:
                return nums[house]
            print(house, n)
            housemem[house] =  max(dfs(house+2)+nums[house], dfs(house+1))
            return housemem[house]

        return max(dfs(0), dfs(1))
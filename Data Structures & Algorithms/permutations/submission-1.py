class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        visited = []

        def dfs():
            if len(visited) == len(nums):
                res.append(visited[:])
                return
            for i in nums:
                if i in visited:
                    continue
                visited.append(i)
                dfs()
                visited.pop(-1)

        dfs()
        return res
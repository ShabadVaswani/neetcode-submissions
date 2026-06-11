class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort();
        res = []
        path = []

        def dfs(start, cursum):
            print(cursum)
            if cursum == target:
                res.append(path[:])
                return
            if cursum>target:
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i, cursum+nums[i])
                print(path)
                path.pop(-1)
        dfs(0, 0)
        return res
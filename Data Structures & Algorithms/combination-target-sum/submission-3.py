class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(bktrk, startindex, cursum):
            if len(nums) < 1 or nums[startindex] > target or cursum > target or cursum == target:
                if cursum == target:
                    res.append(bktrk)
                return
            
            for i in range(startindex, len(nums)):
                dfs(bktrk + [nums[i]], i, cursum+nums[i])
            return 
        dfs([], 0, 0)


        return res
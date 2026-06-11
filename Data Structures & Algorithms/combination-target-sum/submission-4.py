class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        bktrk = []

        def dfs(bktrk, startindex, cursum):
            if startindex >= len(nums) or nums[startindex] > target or cursum > target or cursum == target:
                if cursum == target:
                    res.append(bktrk[:])
                return
            
            for i in range(startindex, len(nums)):
                bktrk.append(nums[i])
                print(bktrk)
                dfs(bktrk, i, cursum+nums[i])
                bktrk.pop(-1)
            return 
        dfs([], 0, 0)


        return res
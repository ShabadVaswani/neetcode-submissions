class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for n in nums]
        res = 1
        for i in range(-1, -len(nums)-1, -1):
            for j in range(len(nums)+i, len(nums)):
                print(i, j, nums[i], nums[j],  dp, nums)
                if nums[j] > nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
                    res = max(dp[i], res)

        return res
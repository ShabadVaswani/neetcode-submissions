class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prefix, postfix = 1, 1
        res = 0
        for i in range(len(nums)):
            prefix = prefix*nums[i]
            postfix = postfix*nums[len(nums)-i-1]
            res = max(prefix, postfix, res)
            if nums[i] == 0:
                prefix = 1
            if nums[len(nums)-i-1] == 0:
                postfix = 1 


        return res
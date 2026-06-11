class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(len(nums) - 1):
            res[i+1] = res[i] * nums[i]
        print(res)
        
        multTillNow = 1
        for i in range(-1, -len(nums)-1, -1):
            res[i] = res[i] * multTillNow
            multTillNow = multTillNow*nums[i]
            print(res[i])
        print(res)
        return res

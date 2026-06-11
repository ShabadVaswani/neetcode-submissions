class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        print(nums)
        i, l, r = 0, 1, len(nums) - 1
        res = []
        while i < len(nums):
            while l < r:
                summ = nums[i] + nums[l] + nums[r]
                if summ == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    r-=1
                    l+=1
                    while l < r and nums[l-1] == nums[l]: l+=1
                if summ > 0:
                    r-=1
                    while r > l and nums[r+1] == nums[r]: r-=1
                if summ < 0: 
                    l+=1
                    while l < r and nums[l-1] == nums[l]: l+=1
            while i < len(nums)-1 and nums[i+1] == nums[i]: i+=1
            i+=1
            l = i+1
            r = len(nums) - 1
        return res

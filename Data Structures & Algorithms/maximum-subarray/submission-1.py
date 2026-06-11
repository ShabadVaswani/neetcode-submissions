class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cursum = 0
        s, l = 0, len(nums)-1
        res = -float('inf')
        res2 = (0,0)
        for i in range(len(nums)):
            cursum += nums[i]
            l=i
            if cursum > res:
                res = cursum
                res2 = (s, l)
            if cursum<0:
                cursum=0
                s = i+1
                l = i+1
            print(cursum, res, cursum > res)
            
        return res
            

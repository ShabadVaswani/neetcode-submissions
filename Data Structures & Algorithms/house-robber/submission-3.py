class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: 
            return nums[0]
        c1, c2 = nums[-2], nums[-1]
        for i in range(n-3, -1, -1):
            print(i, c1, c2)
            
            c1, c2 = max(c1, nums[i] + c2), c1
            

        return max(c1, c2)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = nums[:]
        suffix = nums[:]
        l = len(nums)
        result = nums[:]
        for i in range(1,l):
            prefix[i] = prefix[i-1] * nums[i]
            suffix[-i-1] = suffix[-i] * nums[-i-1]
        for i in range(l):
            if i == 0:
                result[i] = suffix[i+1]
                continue
            if i == l-1:
                result[i] = prefix[i-1]
                continue
            result[i] = prefix[i-1]*suffix[i+1]
        return result
            



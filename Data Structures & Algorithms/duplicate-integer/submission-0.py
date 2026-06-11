class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0;
        while i < len(nums):
            j = 0
            while j < i:
                if nums[j] == nums[i]:
                    return True
                j+=1
            i+=1
        return False
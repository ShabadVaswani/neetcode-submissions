class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0;
        k = nums
        k.sort()
        print(nums)
        while i < len(nums)-1:
            if k[i] == k[i+1]:
                return True
            i+=1
        return False
            
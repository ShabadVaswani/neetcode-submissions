class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = set() # idhar {} nahi chala tha
        for i in nums:
            if i in x:
                return True
            else:
                x.add(i) # idhar append nahi chala tha
        return False
            
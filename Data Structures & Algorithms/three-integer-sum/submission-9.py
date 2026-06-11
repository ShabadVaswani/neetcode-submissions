class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sorting is mandatory
        res = []
        
        # Loop 1: The Anchor (i)
        for i in range(len(nums)):
            # Optimization: If the smallest number is positive, we can't sum to 0
            if nums[i] > 0:
                break
                
            # Duplicate Check: Skip if same as previous anchor
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Set up Two Pointers for the remainder
            l, r = i + 1, len(nums) - 1
            
            # Loop 2: The Two Pointers (l and r)
            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]
                
                if threeSum > 0:
                    r -= 1 # Too big? Make it smaller.
                elif threeSum < 0:
                    l += 1 # Too small? Make it bigger.
                else:
                    # Found a match!
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # Move pointers inward to find MORE pairs for this anchor
                    l += 1
                    r -= 1
                    
                    # Duplicate Check: Skip identical 'l' values
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        
        return res
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')
        while l <= r:
            mid = (l+r)//2
            print(nums[l], nums[mid], nums[r], 'res',res)
            
            if nums[l] > nums[r]:
                if nums[mid] >= nums[l]:
                    l = mid + 1                   
                else:
                    r = mid
            else:
                res = nums[l]
                break
        return res
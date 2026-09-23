class Solution:
                
    def search(self, nums: List[int], target: int) -> int:

        i, j = 0, len(nums) - 1
        
        while i <= j:
            mid = (i+j)//2
            print(mid)

            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[i]:
                if target >= nums[i] and target < nums[mid]:
                    j = mid-1
                else:
                    i = mid+1

            else:
                if target <= nums[j] and target > nums[mid]:
                    i = mid+1
                else:
                    j = mid-1

            print(i,j,mid)


        return -1

        

class Solution:
    def binarysearch(self, nums, target, i, j):
        

        while True:
            curr = (i+j)//2
            if nums[curr] == target:
                return curr

            if j <= i:
                return -1

            if nums[curr] < target:
                i = curr+1

            else:
                j = curr-1
                
    def search(self, nums: List[int], target: int) -> int:

        i, j = 0, len(nums) - 1
        
        while i <= j:
            mid = (i+j)//2
            print(mid)
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                if nums[i] <= nums[mid] and target < nums[i]:
                    i = mid+1
                else:
                    j = mid-1

            else :
                if nums[mid] >= nums[i] or target < nums[i]:
                    i = mid+1
                else:
                    j = mid-1

            if i==j and j==mid:
                break

            print(i,j,mid)


        return -1

        

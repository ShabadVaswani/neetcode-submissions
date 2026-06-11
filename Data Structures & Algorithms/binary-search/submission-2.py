class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = -1
        l = len(nums)-1

        def bsearch(start, end):
            print(start,end, start+(end-start)//2)
            
            
            if nums[start+(end-start)//2] == target:
                return start+(end-start)//2
            if end - start <1:
                return -1
            if nums[start+(end-start)//2]< target:
                print('le')
                return bsearch(start + ((end-start)//2)+1, end)
            elif nums[start+(end-start)//2]> target:
                print('mo')
                return bsearch(start, start+((end-start)//2)-1)
        return bsearch(0,l)
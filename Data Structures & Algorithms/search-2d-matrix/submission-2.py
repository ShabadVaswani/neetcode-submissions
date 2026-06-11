class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = len(matrix[0])
        nums = []
        for i in matrix:
            if target <= i[-1]:
                nums = i
                break
        if not nums: return False

        
        i = False
        l = len(nums)-1

        


        def bsearch(start, end):
            print(start,end, start+(end-start)//2)
            
            
            if nums[start+(end-start)//2] == target:
                return True
            if end - start <1:
                return False
            if nums[start+(end-start)//2]< target:
                print('le')
                return bsearch(start + ((end-start)//2)+1, end)
            elif nums[start+(end-start)//2]> target:
                print('mo')
                return bsearch(start, start+((end-start)//2)-1)
        return bsearch(0,l)
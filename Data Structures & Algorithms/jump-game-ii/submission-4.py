class Solution:
    def jump(self, nums: List[int]) -> int:
        i = 0
        l = 1
        r = 0
        rf = 0
        jump = 0
        while i < len(nums)-1:
            temp = i
            while i<=r:
                rf = max(rf, i+nums[i])
                print(rf)
                i += 1
            jump +=1
            
            if rf >= len(nums)-1:
                return jump
            r = rf
            i = l
            l = r+1
            print(l,r,i)
            if temp == i:
                break
        return jump
            
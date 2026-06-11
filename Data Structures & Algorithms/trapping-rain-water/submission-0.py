class Solution:
    def trap(self, height: List[int]) -> int:
        maxl = height[0]
        l = 0
        maxr = height[len(height)-1]
        r = len(height)-1
        sumi = 0
        while l < r:
            if maxl <= maxr:
                if maxl - height[l]>0:
                    sumi += maxl - height[l]
                l+=1
            else:
                if maxr - height[r]>0:
                    sumi += maxr - height[r]
                r-=1
            
            if height[l] > maxl:
                maxl = height[l]
            if height[r] > maxr:
                maxr = height[r]

        return sumi
        



        
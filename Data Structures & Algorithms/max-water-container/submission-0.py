class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            for j in range(i+1,len(heights)):
                h = min(heights[i], heights[j])
                l = j - i
                if h*l > maxArea: maxArea = h*l
        return maxArea

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, h in enumerate(heights):
            lastpop = i
            print(stack)
            while len(stack)>0 and h < stack[-1][1]:
                lastpop, tempheight = stack.pop()
                print(lastpop, tempheight)
                if (i-lastpop)*tempheight>res:
                    res = (i-lastpop)*tempheight
            if len(stack) == 0 or h > stack[-1][1]:
                stack.append([lastpop, h])
        while stack:
            print(stack)
            i, h = stack.pop()
            print()
            if (len(heights) - i)*h> res:
                res = (len(heights) - i)*h 
                print('res', res)
        return res
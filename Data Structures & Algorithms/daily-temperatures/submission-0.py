class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][0]< t:
                stackidx = stack[-1][1]
                res[stackidx] = i - stackidx
                stack.pop()

            stack.append([t,i])
        return res
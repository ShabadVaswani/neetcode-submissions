class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i, temp in enumerate(temperatures):
            element = [i, temp]
            
            while len(stack)!=0 and temp > stack[-1][1]:
                tempi, temptemp = stack.pop()
                res[tempi] = i - tempi
            if len(stack) == 0 or temp <= stack[-1][1]:
                stack.append(element)
        return res
                



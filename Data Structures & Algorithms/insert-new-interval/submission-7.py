class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        newStart, newEnd = newInterval[0], newInterval[1]
        res = []
        for index, [start, end] in enumerate(intervals):
            if newEnd < start:
                res.append([newStart, newEnd])
                return res + intervals[index:]
            elif newStart > end:
                res.append([start, end])
            else:
                newStart, newEnd = min(start, newStart), max(end, newEnd)
        res.append([newStart, newEnd])
        return res  


                
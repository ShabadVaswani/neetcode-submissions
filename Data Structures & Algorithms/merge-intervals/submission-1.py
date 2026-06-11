class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newStart, newEnd = intervals[0][0], intervals[0][1]
        res = []
        index = 0
        lenint = len(intervals)
        while index<lenint:
            start, end = intervals[index][0], intervals[index][1]
            print(start)
            if newEnd < start:
                res.append([newStart, newEnd])
                newStart, newEnd = start, end
            else:
                newStart, newEnd = min(start, newStart), max(end, newEnd)
            index+=1
        res.append([newStart, newEnd])
        return res  


                
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        newStart, newEnd = intervals[0][0], intervals[0][1]
        res = []
        for index, [start, end] in enumerate(intervals):
            print(start)
            if newEnd < start:
                res.append([newStart, newEnd])
                newStart, newEnd = start, end
            else:
                newStart, newEnd = min(start, newStart), max(end, newEnd)
        res.append([newStart, newEnd])
        return res  


                
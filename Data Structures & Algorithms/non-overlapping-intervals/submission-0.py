class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = []
        cnt = 0
        oldStart, oldEnd = intervals[0][0], intervals[0][1]
        for index, [start, end] in enumerate(intervals[1:]):
            if oldEnd <= start:
                res.append([oldStart, oldEnd])
                oldStart, oldEnd = start, end
            else:
                cnt+=1
                if end < oldEnd:
                    res.append([start, end])
                    oldStart, oldEnd = start, end
                else:
                    print('hw')
                    res.append([oldStart, oldEnd])
                    
        print(res)
        return cnt

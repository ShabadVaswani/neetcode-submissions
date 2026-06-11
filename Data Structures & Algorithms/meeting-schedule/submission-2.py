"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if intervals == []:
            return True
        nintervals = []
        for i in intervals:
            nintervals.append([i.start, i.end])
        nintervals.sort()
        preEnd = nintervals[0][1]
        for start, end in nintervals[1:]:
            print(start, nintervals[0][1], preEnd)
            if start >= preEnd:
                preEnd = max(preEnd, end)
            else:
                return False
        return True

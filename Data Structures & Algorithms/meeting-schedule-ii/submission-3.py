"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if intervals == []:
            return 0
        nintervals = []
        for i in intervals:
            nintervals.append([i.start, i.end])
        nintervals.sort()
        maxHeap = []
        for start, end in nintervals:
            heapq.heappush(maxHeap, end)
            if maxHeap[0] <= start:
                heapq.heappop(maxHeap)
            

        return len(maxHeap)
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        cpq = queries.copy()
        cpq.sort()
        minheap = []
        res = queries.copy()
        cres = {}
        newStart = 0
        for q in cpq:
            for i in range(newStart, len(intervals)):
                start, end = intervals[i][0],intervals[i][1]
                if start <= q:
                    heapq.heappush(minheap, [end - start + 1, end])
                    newStart+=1
                else:
                    break

            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            if minheap:
                cres[q] = minheap[0][0]
            else:
                cres[q] = -1

        for i, val in enumerate(queries):
            res[i] = cres[val]
        return res

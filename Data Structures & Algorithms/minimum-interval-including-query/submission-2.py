class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        cpq = queries.copy()
        cpq.sort()
        minheap = []
        res = queries.copy()
        cres = {}
        for q in cpq:
            print("\n\n", q)
            for i, [start, end] in enumerate(intervals):
                if start <= q:
                    print(q, start, end, end-start+1, q <=start)
                    heapq.heappush(minheap, [end - start + 1, end])
                    intervals = intervals[1:]

            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            if minheap:
                cres[q] = minheap[0][0]
            else:
                cres[q] = -1

        for i, val in enumerate(queries):
            res[i] = cres[val]
        return res

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        cpq = queries.copy()
        cpq.sort()
        minheap = []
        res = queries.copy()
        cres = [0 ]* 10000
        for q in cpq:
            print("\n\n", q)
            for start, end in intervals:
                if start <= q:
                    print(q, start, end, end-start+1, q <=start)
                    heapq.heappush(minheap, [end - start + 1, end])

            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)
            if minheap:
                cres[q] = minheap[0][0]
            else:
                cres[q] = -1

        for i, val in enumerate(queries):
            res[i] = cres[val]
        return res

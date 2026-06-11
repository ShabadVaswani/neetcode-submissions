class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res={}
        i=0
        minHeap=[]
        for q in sorted(queries):
            while i<len(intervals) and q >= intervals[i][0]:
                left=intervals[i][0]
                right=intervals[i][1]
                heapq.heappush(minHeap,(right-left+1,right))
                i+=1
            while minHeap and q > minHeap[0][1]:
                heapq.heappop(minHeap)
            res[q]=minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]

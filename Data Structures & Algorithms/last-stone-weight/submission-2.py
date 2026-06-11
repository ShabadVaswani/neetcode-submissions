class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) > 1:
            l1 = -heapq.heappop(max_heap)
            l2 = -heapq.heappop(max_heap)

            res = abs(l1-l2)

            if res == 0:
                continue
            heapq.heappush(max_heap, -res)
        if not max_heap:
            return 0
        return -heapq.heappop(max_heap)
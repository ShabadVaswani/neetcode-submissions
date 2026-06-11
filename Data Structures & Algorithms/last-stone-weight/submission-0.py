class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            s1 = -heapq.heappop(stones)
            s2 = -heapq.heappop(stones)

            newStone = abs(s1-s2)
            if newStone > 0:
                heapq.heappush(stones,-newStone)
            print(stones)

        if len(stones)==0: return 0
        print(stones)
        return -stones[0]

            
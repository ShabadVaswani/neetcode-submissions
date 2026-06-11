class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hmap = defaultdict(int)

        for i in  hand:
            if i in hmap:
                hmap[i] += 1
            else:
                hmap[i] = 1
        min_heap = list(hmap.keys())
        heapq.heapify(min_heap)

        while min_heap:
            mini = min_heap[0]
            for i in range(groupSize):
                if i + mini not in hmap:
                    return False
                hmap[i+mini]-=1
                if hmap[i+mini] == 0:
                    heapq.heappop(min_heap)


            
            
        return True

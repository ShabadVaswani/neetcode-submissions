class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        listwithdist = []
        for (x,y) in points:
            dist = x ** 2 + y ** 2
            listwithdist.append([dist,x,y])
        heapq.heapify(listwithdist)
        res = []
        while k:
            d,x,y = heapq.heappop(listwithdist)
            res.append([x,y])
            k-=1
        return res

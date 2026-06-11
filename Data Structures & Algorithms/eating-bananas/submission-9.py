class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        l, r = 1, piles[len(piles) - 1]
        res = float("inf")
        while l <= r:
            mid = (l+r)//2
            
            # calculating total time taken
            totalTime = 0
            for pile in piles:
                totalTime += math.ceil(pile/mid)
            if totalTime <= h:
                res = min(mid, res)
                r = mid - 1
            else:
                l = mid + 1
        return res

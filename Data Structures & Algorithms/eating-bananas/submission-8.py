class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0]/h)
        maxpile = max(piles)
        l, r = 1, maxpile
        res = float('inf')
        while l < r:
            currate = math.ceil((l+r)/2)
            totalhr = 0
            for pile in piles:
                totalhr += math.ceil(pile/currate)
            print(totalhr, h, res, totalhr <= h)
            print(l, r, currate)
            if totalhr <= h:
                res = min(res, currate)
                r = currate - 1
            else:
                l = currate 

        return res

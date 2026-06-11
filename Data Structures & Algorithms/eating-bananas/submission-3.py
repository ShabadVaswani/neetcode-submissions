class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)
        res = r
        while l <= r:
            mid = (l+r)//2
            
            total = sum((pile + mid - 1) // mid for pile in piles)

            if total <= h:
                r = mid-1
                res=mid
            elif total > h:
                l = mid+1
        return res

            
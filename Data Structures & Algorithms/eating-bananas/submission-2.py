class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        mx = max(piles)
        l = 1
        r = mx
        mid = 0
        minmiddone = mx
        while l <= r:
            mid = (l+r)//2
            total = 0
            for i in piles:
                time = i//mid
                if time < i/mid: time+=1
                total+=time
                print('kk', i,mid, total)
            print(mid, total)

            if total <= h:
                r = mid-1
                if minmiddone>mid:
                    minmiddone=mid
            elif total > h:
                l = mid+1
        return minmiddone

            
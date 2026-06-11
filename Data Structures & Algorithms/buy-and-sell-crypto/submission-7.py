class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        res = 0
        while l < len(prices) :
            while r < len(prices) :
                diff = prices[r] - prices[l]
                if diff <= 0:
                    l = r
                print(l,r)
                res = max(res, diff)
                r+=1

            l +=1
            r = l+1
        return res
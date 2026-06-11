class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar = prices[0]
        maxprofit = 0
        for i in prices:
            minsofar = min(minsofar,i)
            if i - minsofar > maxprofit:
                maxprofit = i - minsofar
            
        return maxprofit
        


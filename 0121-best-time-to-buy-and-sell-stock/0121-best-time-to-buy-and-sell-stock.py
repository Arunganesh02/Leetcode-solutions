class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1
        maxi = 0 
        while r<len(prices):
            if prices[l] >= prices[r]:
                l = r
            elif prices[r] > prices[l]:
                maxi = max(maxi , prices[r] - prices[l])
            r += 1
        return maxi
     



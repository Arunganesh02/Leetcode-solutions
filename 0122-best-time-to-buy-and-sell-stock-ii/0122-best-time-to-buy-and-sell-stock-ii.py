class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        def traverse(indi , buy):
            if indi == len(prices):
                return 0
            if dp[indi][buy] != -1 : return dp[indi][buy]
            if buy == 1:
                profit = max(-prices[indi] + traverse(indi+1 , 0) , traverse(indi+1 , 1))
            else:
                profit = max(prices[indi] + traverse(indi+1,1) , traverse(indi+1 ,0))
            dp[indi][buy] = profit
            return dp[indi][buy]
        dp = [[-1 for i in range(2)] for j in range(len(prices))]

        return traverse(0 , 1)

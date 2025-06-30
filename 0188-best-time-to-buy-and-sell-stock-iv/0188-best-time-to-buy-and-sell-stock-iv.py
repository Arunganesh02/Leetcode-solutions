class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        dp = [[[0 for i in range(k+1)] for j in range(2)] for p in range(len(prices)+1)]


        for indi in range(len(prices)-1 , -1 , -1):
            for buy in range(2):
                for cap in range(1,k+1):
                    if (buy):
                        profit = max(-prices[indi] + dp[indi+1][0][cap] , dp[indi+1][1][cap])
                    else:
                        profit = max(prices[indi] + dp[indi+1][1][cap-1] , dp[indi+1][0][cap])
                    dp[indi][buy][cap] = profit

        return dp[0][1][k]        
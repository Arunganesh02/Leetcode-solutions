class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        co = float('inf')
        coins.reverse()
        def traverse(indi , su):
            # if su == 0 : return 1
            if indi == 0 :
                if su%coins[0] == 0 : return su//coins[0]
                else: return float('inf')
            if dp[indi][su] != -1 : return dp[indi][su]
            nottake = float('inf')
            nottake = 0 + traverse(indi-1 , su)
            take = float('inf')
            if coins[indi] <= su:
                take = 1 + traverse(indi , su-coins[indi])
            dp[indi][su] = min(nottake , take)
            return min(nottake , take)
        dp = [[-1 for i in range(amount+1)] for j in range(len(coins))]
        ans = traverse(len(coins)-1 , amount)
        if ans == float('inf') : return -1
        else: return ans
        # return traverse(len(coins)-1 , amount)
        # if co == float('inf'): return -1
        # return co
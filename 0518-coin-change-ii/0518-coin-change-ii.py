class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        def traverse(indi , su):
            if su == 0 : return 1
            if indi ==0 :
                if su % coins[indi] == 0 : return 1
                else: return 0
            take = nottake = 0
            if dp[indi][su] != -1 : return dp[indi][su]
            nottake = traverse(indi-1 , su)
            if coins[indi] <= su:
                take = traverse(indi , su-coins[indi])
            dp[indi][su] = take + nottake
            return take + nottake

    
        dp = [[-1 for i in range(amount+1)] for j in range(len(coins))]
        return traverse(len(coins)-1 , amount)
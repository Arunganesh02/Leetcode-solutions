class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        c = len(nums)
        nums.insert(0,1)
        nums.append(1)

        def traverse(i , j):
            if i> j : return 0
            maxi = float('-inf')
            if dp[i][j] != -1 : return dp[i][j]
            for k in range(i,j+1):
                coins = (nums[i-1] * nums[k] * nums[j+1]) + traverse(i , k-1 ) + traverse(k+1 , j)
            
                maxi = max(coins , maxi)
            dp[i][j] = maxi
            return maxi
        dp = [[-1 for i in range(len(nums))] for j in range(len(nums))]
        return traverse(1 , c)
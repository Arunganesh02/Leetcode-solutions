class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        def traverse(i , j):
            if i==0 and j == 0: return 1
            if i==-1 or j== -1 : return 0
            # print(i , j)
            if dp[i][j] != -1 : return dp[i][j]
            left = traverse(i , j-1)
            up = traverse(i-1 , j)
            dp[i][j] = left + up
            return left + up
        
        dp = [[-1 for i in range(n)] for j in range(m)]
        # traverse(m-1 , n-1)
        # print(dp)
        return traverse(m-1 , n-1)
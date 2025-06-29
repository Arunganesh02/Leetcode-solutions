class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        def traverse(i , j ):
            if j<0 : return 1
            if i<0 : return 0
            if dp[i][j] != -1 : return dp[i][j]
            if s[i] == t[j]:
                ans = traverse(i-1 , j-1) + traverse(i-1,j)
            else:
                ans = traverse(i-1 , j)
            dp[i][j] = ans
            return ans
        dp = [[-1 for i in range(len(t))] for j in range(len(s))]
        return traverse(len(s)-1 , len(t)-1)
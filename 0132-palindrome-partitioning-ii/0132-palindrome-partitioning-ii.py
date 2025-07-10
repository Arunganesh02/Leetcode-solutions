class Solution:
    def minCut(self, s: str) -> int:
        def traverse( i , j):
            if i == j : return 0
            if i>j : return 0
            mini = float("inf")
            if dp[i][j] != -1 : return dp[i][j]
            for k in range(i , j):
                if s[i:k+1] == s[i:k+1][::-1]:
                    cuts = 1 + traverse(k+1 , j)
                    mini = min(cuts , mini)
            dp[i][j] = mini
            return mini
        dp = [[-1 for i in range(len(s)+1)] for j in range(len(s)+1)]
        return traverse(0 , len(s))-1
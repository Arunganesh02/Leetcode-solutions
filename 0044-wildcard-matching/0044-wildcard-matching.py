class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        def traverse(i , j):

            if i<0 and j<0 : return True
            if j<0 and i >= 0: return False
            if i<0 and j>=0 : 
                for ii in range(0 , j+1):
                    if p[ii] != "*":
                        return False
                return True
            if dp[i][j] != -1 : return dp[i][j]
            ans1 = ans2 = False
            if s[i] == p[j] or p[j] == "?":
                ans1 = traverse(i-1 , j-1)

            else:
                if p[j] == "*":
                    ans2 = traverse(i-1 , j)  or traverse(i , j-1)
            dp[i][j] = ans1 or ans2
            return dp[i][j]
        dp = [[-1 for i in range(len(p))] for j in range(len(s))]
        return traverse(len(s)-1 , len(p)-1)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        text1 = word1
        text2 = word2
        dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        for i in range(1 , len(text1)+1):
            for j in range(1 , len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        if len(text1)> len(text2):
            ans = len(text1) - dp[len(text1)][len(text2)]
            ans += len(text2) - dp[len(text1)][len(text2)]
        else:
            ans = len(text2) - dp[len(text1)][len(text2)]
            ans += len(text1) - dp[len(text1)][len(text2)]            
        return ans
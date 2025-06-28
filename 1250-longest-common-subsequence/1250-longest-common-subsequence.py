class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def traverse(ind1 , ind2 ):
            nonlocal dp
            if ind1<0 or ind2<0 :
                return 0
            if dp[ind1][ind2] != -1 : return dp[ind1][ind2]
            if text1[ind1] == text2[ind2]:                
                var = 1+ traverse(ind1-1 , ind2-1)
            else:
                var = max(traverse(ind1-1 , ind2) , traverse(ind1 , ind2-1))
            dp[ind1][ind2] = var
            return var
        dp = [[-1 for i in range(len(text2))] for j in range(len(text1))]
        return traverse(len(text1)-1 , len(text2)-1)
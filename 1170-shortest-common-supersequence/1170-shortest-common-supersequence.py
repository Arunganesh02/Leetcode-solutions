class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        text1 = str1
        text2 = str2
        dp = [[0 for i in range(len(text2)+1)] for j in range(len(text1)+1)]
        for i in range(1 , len(text1)+1):
            for j in range(1 , len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
        common = dp[len(str1)][len(str2)]
        st = ""
        i , j = len(str1) , len(str2)
        while i>0 and j > 0 :
            if text1[i-1] == text2[j-1]:
                st += text1[i-1]
                i -= 1
                j -= 1
            else:
                if dp[i-1][j] > dp[i][j-1]:
                    st += text1[i-1]
                    i -= 1 
                else:
                    st += text2[j-1]
                    j -= 1
        print(i , j)
        if i>0 : 
            while i!=0:
                st += text1[i-1]
                i -= 1
        if j>0 : 
            while j != 0:
                st += text2[j-1]
                j -= 1
        st = st[::-1]
        return st
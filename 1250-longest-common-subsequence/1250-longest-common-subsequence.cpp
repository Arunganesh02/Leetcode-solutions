class Solution {
public:
    int traverse(int indi1 , int indi2 , string &text1 , string &text2 , vector<vector<int>> &dp){
        if(indi1 <0 || indi2<0)  return 0;

        if (indi1 == 0 && indi2 == 0){
            if (text1[indi1] == text2[indi2]) return 1;
            else return 0 ;
        }

        if (dp[indi1][indi2] != -1) return dp[indi1][indi2];
        int count;

        if (text1[indi1] == text2[indi2]) count = 1 + traverse(indi1-1 , indi2 - 1 , text1 , text2 , dp);

        else 
        count = max(traverse(indi1-1 , indi2, text1, text2,dp),traverse(indi1 , indi2-1 , text1 , text2 , dp)) ;

        return dp[indi1][indi2] = count;
    }
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>> dp(text1.size()+1 , vector<int> (text2.size()+1,0));
        int count ; 
        // if (text1[0] == text2[0]) dp[0][0] = 1;
        for (int i = 1 ; i<=text1.size() ; i++){
            for (int j =1;j<=text2.size() ; j++){
                if (text1[i-1] == text2[j-1]){
                    count = 1 + dp[i-1][j-1];
                }
                else{
                    count = max(dp[i-1][j], dp[i][j-1]);
                }
                dp[i][j] = count;
            }
        }
        return dp[text1.size()][text2.size()];
        // return traverse(text1.size()-1 , text2.size()-1 , text1 , text2 , dp);
    }
};
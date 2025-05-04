class Solution {
public:
    int traverse(int indi1 , int indi2 , string &text1 , string &text2 , vector<vector<int>> &dp){
        if(indi1 <0 || indi2<0)  return 0;
        if (indi1 == 0 && indi2 == 0){
            if (text1[indi1] == text2[indi2]) return 1;
            else return 0 ;
        }
        if (dp[indi1][indi2] != -1) return dp[indi1][indi2];
        int count ;
        // cout<<text1[indi1]<<" "<<text2[indi2]<<'\n';
        if (text1[indi1] == text2[indi2]){
            count = 1 + traverse(indi1-1 , indi2 - 1 , text1 , text2 , dp);
        }
        else count = traverse(indi1-1 , indi2 , text1 , text2 , dp);

        return dp[indi1][indi2] = max(count ,traverse(indi1 , indi2-1 , text1 , text2 , dp));
    }
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>> dp(text1.size() , vector<int> (text2.size(),-1));
        return traverse(text1.size()-1 , text2.size()-1 , text1 , text2 , dp);
    }
};
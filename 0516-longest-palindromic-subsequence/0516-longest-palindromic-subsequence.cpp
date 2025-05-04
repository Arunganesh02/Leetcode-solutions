class Solution {
public:
    int lcs(string text1, string text2) {
        vector<vector<int>> dp(text1.size()+1 , vector<int> (text2.size()+1,0));
        int count ; 
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
    }
    // int traverse(int indi , string& s){
    //     if (indi == 0) return 1;

    //     int count; 
    //     int maxi = INT_MIN;
    //     for (int i = indi-1 ; i>-1 ; i--){
    //         sub = substr(0 ,s )
    //         count = lcs()
    //         maxi = max(count , maxi);
    //     }
    //     return maxi;
    // }
    int longestPalindromeSubseq(string s) {
        string cp = s;
        reverse(s.begin() , s.end());
        return lcs(cp, s);
    }
};
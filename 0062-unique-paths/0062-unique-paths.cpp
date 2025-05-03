class Solution {
public:
    int traverse(int i , int j ,vector<vector<int>> &dp){
        if (i==0 && j==0) return 1;
        if (i<0 || j<0) return 0;
        if (dp[i][j] != -1) return dp[i][j];
        int up = 0;
        int left = 0;
        up = traverse(i-1 , j , dp);
        left = traverse(i , j-1 , dp);
        dp[i][j] = up+left;
        return up+left;
    }
    int uniquePaths(int m, int n) {
        vector<vector<long long>> dp(m + 1, vector<long long>(n + 1, -1));
        dp[0][0] = 1;
        long long up ,left ;
        for (int i = 0 ; i<=m;i++){
            for (int j = 0 ; j<=n;j++){
                up = 0;
                left = 0;
                if (i-1 >= 0 ){
                    up = dp[i-1][j];
                }
                if (j-1 >= 0){
                    left = dp[i][j-1];
                }
                if (i==0 && j== 0);
                else dp[i][j] = left + up;
            }
        }
        return dp[m-1][n-1];

    }
};
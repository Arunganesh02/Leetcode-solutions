class Solution {
public:
    int climbStairs(int n) {
        vector<int> dp(2 , -1);
        dp[0] = 0;
        dp[1] = 1;
        if (n==1) return 1;
        int ans;
        for (int i = 2 ; i<=n+1 ; i++){
            ans = dp[0] + dp[1];
            dp[0] = dp[1];
            dp[1] = ans;
        }
        return dp[1];
    }
};
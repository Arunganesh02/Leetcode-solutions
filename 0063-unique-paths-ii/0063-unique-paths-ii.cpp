class Solution {
public:
    int traverse(int i , int j , vector<vector<int>>& obstacleGrid , vector<vector<long long>> &dp){
        if (i<0 || j<0) return 0;
        if (obstacleGrid[i][j] == 1)  return 0;
        if (i==0 && j == 0) return 1;


        if (dp[i][j] != -1) return dp[i][j];
        int up =0 ;
        int left = 0;
        up = traverse(i-1 , j , obstacleGrid , dp);
        left = traverse(i , j-1 , obstacleGrid , dp);
        dp[i][j] = up+left;
        return up + left ;
    }
    int uniquePathsWithObstacles(vector<vector<int>>& obstacleGrid) {
        vector<vector<long long>> dp(obstacleGrid.size() , vector<long long>(obstacleGrid[0].size() , -1)) ;
        return traverse(obstacleGrid.size()-1 , obstacleGrid[0].size()-1 , obstacleGrid , dp);
    }
};
class Solution {
public:

    int traverse(int i , int j , vector<vector<int>> &grid , vector<vector<int>> &dp){
        if (i ==0 && j == 0 ) return grid[i][j];

        int up = INT_MAX , left = INT_MAX;
        if (dp[i][j] != -1) return dp[i][j];
        if (i-1 >=0) up = grid[i][j] + traverse(i-1 , j , grid , dp);
        if (j-1 >=0)left = grid[i][j] + traverse(i , j-1 , grid , dp); 
        
        return dp[i][j] = min(up , left );

    }
    int minPathSum(vector<vector<int>>& grid) {
        vector<vector<int>> dp(grid.size() +1,vector<int>(grid[0].size(),-1));
        return traverse(grid.size()-1 , grid[0].size()-1 , grid , dp);
    }
};
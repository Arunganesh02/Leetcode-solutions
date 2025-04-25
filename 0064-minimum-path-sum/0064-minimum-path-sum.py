class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def traverse(i , j):
            if i ==0 and j == 0 : return grid[i][j]
            if i== -1 or j == -1 : return -1
            if dp[i][j] != -1 : return dp[i][j]

            left = grid[i][j] + traverse(i , j-1)
            up = grid[i][j]+ traverse(i-1 , j)
            if up == grid[i][j]-1:
                dp[i][j] = left
            elif left == grid[i][j]-1:
                dp[i][j] = up
            else:
                dp[i][j] = min(left , up)

            return dp[i][j]

        dp = [[-1 for i in range(len(grid[0]))] for j in range(len(grid))]

        traverse(len(grid)-1, len(grid[0])-1)
        # print(dp)
        return traverse(len(grid)-1, len(grid[0])-1)
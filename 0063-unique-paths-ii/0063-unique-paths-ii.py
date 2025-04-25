class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def traverse(i , j):
            if obstacleGrid[i][j] == 1 : return 0
            if i ==0 and j == 0: return 1
            if i == -1 or j == - 1: return 0
            if dp[i][j] != -1 : return dp[i][j]
            left = traverse(i , j-1)
            up = traverse(i-1 , j)
            dp[i][j] = left + up
            return left + up
        dp = [[-1 for i in range(len(obstacleGrid[0]))] for j in range(len(obstacleGrid))]
        return traverse(len(obstacleGrid)-1 , len(obstacleGrid[0])-1)
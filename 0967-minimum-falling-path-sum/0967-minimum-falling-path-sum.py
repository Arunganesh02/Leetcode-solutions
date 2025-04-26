class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def traverse(i , j ):
            if j < 0 or j >= len(matrix):
                return float('inf')
            if i == 0 : return matrix[0][j]

            if dp[i][j] != float('inf') : return dp[i][j]

            bef = matrix[i][j] + traverse(i-1,j-1)
            curr = matrix[i][j] + traverse(i-1 , j)
            aft = matrix[i][j] + traverse(i-1 ,j+1)
            minim = min(bef , curr , aft)
            dp[i][j] = minim
            return minim
        mini = float("inf")
        dp = [[float("inf") for i in range(len(matrix))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            mini = min(mini , traverse(len(matrix)-1, i))
        return mini
        
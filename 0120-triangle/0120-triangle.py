class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def traverse(i , j ):
            if i == 0 : return triangle[0][0]
            if j>=len(triangle): return float('inf')
            if dp[i][j] != 100000 : return dp[i][j]
            same, diff = 1000000 , 1000000
            if j < len(triangle[i-1]):
                same = triangle[i][j] + traverse(i-1 , j)
            if j-1 > -1:
                diff = triangle[i][j] + traverse(i-1 , j-1)
            mini = min(same , diff)
            dp[i][j] = mini
            return mini

        dp = [[100000 for i in range(len(triangle))] for j in range(len(triangle))]
        minim = float('inf')
        for i in range(len(triangle[-1])):
            minim = min(minim ,traverse(len(triangle)-1 , i))

        return minim
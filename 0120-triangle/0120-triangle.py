class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def traverse(i , j ):
            if i == 0 : 
                # print(triangle[0][0])
                dp[0][0] = triangle[0][0]
                return triangle[0][0]
            if j>=len(triangle): return 0
            mini = float('inf')
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

        for i in range(len(triangle[-1])):
            traverse(len(triangle)-1 , i)


        return min(dp[len(triangle)-1])
class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        p = len(cuts)
        cuts.insert(0,0)
        cuts.append(n)
        cuts.sort()
        def traverse(i , j ):
            if i>j : return 0
            mini = float('inf')
            if dp[i][j] != -1 : return dp[i][j]
            for k in range(i,j+1):
                cu = cuts[j+1] - cuts[i-1] + traverse(i , k-1 ) + traverse(k+1 , j)
                mini = min(mini , cu)
            dp[i][j] = mini
            return mini
        dp = [[-1 for i in range(len(cuts))] for j in range(len(cuts))]
        return traverse(1 , p)


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        def traverse(i):

            if i==len(arr): return 0
            ma = arr[i]
            c = 0
            maxi = float("-inf")
            if dp[i] != -1 : return dp[i]
            for p in range(i,min(i+k,len(arr))):
                c += 1
                ma = max(ma , arr[p])
                su = (ma*c) + traverse(p+1 )
                maxi = max(su , maxi)

            dp[i] = maxi
            return maxi
        dp = [-1 for i in range(len(arr))]
        return traverse(0)
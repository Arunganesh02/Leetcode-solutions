class Solution:
    def jump(self, nums: List[int]) -> int:
        def traverse(indi):
            # if indi >
            if indi >= len(nums) : return 0
            if indi == len(nums)-1:
                return 0
            if dp[indi] != -1 : return dp[indi]
            mi = float('inf')
            # print(indi)
            for i in range(indi + 1, indi+nums[indi]+1):
                mi = min(mi , 1+traverse(i))
            dp[indi] = mi
            return mi

        dp = [-1 for i in range(len(nums)+1)]
        return traverse(0)
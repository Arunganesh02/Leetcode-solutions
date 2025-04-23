class Solution:
    def rob(self, nums: List[int]) -> int:
        def traverse(start):
            if start < 0 : return 0
            if dp[start] != -1 : return dp[start]
            steal = nums[start] + traverse(start-2)
            leave = traverse(start-1)
            dp[start] = max(steal , leave)
            return dp[start]

        dp = [-1] * len(nums)
        maxi = 0
        return traverse(len(nums)-1)
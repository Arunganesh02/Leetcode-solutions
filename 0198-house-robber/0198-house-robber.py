class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 : return nums[0]
        if len(nums) == 2 : return max(nums)
        def traverse(start):
            if start == 0: return nums[0]
            if start == 1: return nums[1]
            if dp[start] != -1 : return dp[start]
            li = []
            for i in range(start-2 , -1  , -1):
                li.append(traverse(i))
            # print(li)
            dp[start] = max(li) + nums[start]
            return dp[start]

        dp = [-1] * len(nums)
        dp[0] = nums[0]
        dp[1] = nums[1]
        for i in range(len(nums)-1 , -1 , -1):
            traverse(i)
        return max(dp)
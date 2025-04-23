class Solution:
    def rob(self, nums: List[int]) -> int:
        def traverse(start):
            if start == 0: 
                dp[start] =  nums[0]
                return nums[0]
            if start == 1:
                dp[start] = nums[1]
                return nums[1]
            if dp[start] != -1 : return dp[start]
            li = []
            for i in range(start-2 , -1  , -1):
                li.append(traverse(i))
            dp[start] = max(li) + nums[start]
            return dp[start]

        dp = [-1] * len(nums)
        for i in range(len(nums)-1 , -1 , -1):
            traverse(i)
        return max(dp)
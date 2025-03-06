class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            maxi = nums[i]
            mini = nums[i]
            for j in range(i+1 , len(nums)):
                maxi = max(maxi  , nums[j])
                mini = min(mini, nums[j])
                ans += maxi - mini

        return ans
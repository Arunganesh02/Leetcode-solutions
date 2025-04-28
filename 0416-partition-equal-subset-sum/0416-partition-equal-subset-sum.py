class Solution(object):
    def canPartition(self, nums):
        tot = sum(nums)
        def traverse(indi , tar):
            if tar == 0 : return True
            if indi == 0 : return nums[indi] == tar
            if dp[indi][tar] != None : return dp[indi][tar]
            take = False
            nottake = traverse(indi -1 , tar)
            if nums[indi] <= tar:
                take = traverse(indi -1 , tar - nums[indi])
            dp[indi][tar] = nottake or take
            return nottake or take
        dp = [[None for i in range((sum(nums)//2)+1)] for j in range(len(nums))]
        if sum(nums) % 2 ==0:
            return traverse(len(nums)-1 , sum(nums)//2)
        else: return False
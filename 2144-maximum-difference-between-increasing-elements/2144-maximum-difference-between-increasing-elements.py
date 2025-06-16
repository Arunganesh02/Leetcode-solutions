class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        # c = -1
        # for i in range(len(nums)):
        #     for j in range(i+1 , len(nums)):   
        #         if nums[i] < nums[j]:
        #             c = max(c , nums[j] - nums[i])
        # return c

        mi = nums[0]
        diff = -1
        for i in range(1,len(nums)):
            if mi < nums[i]:
                diff = max(diff , nums[i] - mi)
            mi = min(mi , nums[i])
        return diff
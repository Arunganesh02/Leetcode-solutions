class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = 0
        # for i in range(len(nums)):
        #     for j in range(i+1 , len(nums)):
        #         for k in range(j+1 , len(nums)):
        #             ans = max(ans ,(nums[i] - nums[j]) * nums[k])


        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                he = nums[j+1:]
                heapq._heapify_max(he)
                if j != len(nums) -1:
                    ans = max(ans , (nums[i] - nums[j]) * he[0])


        return ans
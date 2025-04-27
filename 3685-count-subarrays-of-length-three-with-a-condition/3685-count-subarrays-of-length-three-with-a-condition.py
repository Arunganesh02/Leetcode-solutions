class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0 
        left = nums[0]
        mid = nums[1]
        r = 2
        while r<len(nums):
            right = nums[r]
            if left + right == mid/2:
                count += 1
            left = mid
            mid = right
            r+= 1
        return count
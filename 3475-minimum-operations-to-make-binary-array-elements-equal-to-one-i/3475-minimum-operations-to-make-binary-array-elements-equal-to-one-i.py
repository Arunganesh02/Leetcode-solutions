class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        for i in range(len(nums)-2):
            if nums[i] == 0:
                ops += 1
                nums[i] = 1
                for j in range(i+1 , i+3):
                    if nums[j] == 0: nums[j] = 1
                    else: nums[j] = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                return -1
        return ops
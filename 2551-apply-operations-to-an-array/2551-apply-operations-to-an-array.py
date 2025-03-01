class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(1 , len(nums)):
            if nums[i] ==  nums[i-1]:
                nums[i] = 0
                nums[i-1] *= 2
        
        l = 0
        r = 1
        while r<len(nums):
            if nums[l] != 0:
                l += 1 
            elif nums[l] == 0 and nums[r] != 0:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
            elif nums[r] == 0:
                r += 1
                continue
            else:
                l += 1
            r += 1
            
        return nums
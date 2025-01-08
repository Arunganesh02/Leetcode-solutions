class Solution:
    def check(self, nums: List[int]) -> bool:
        l = 0
        r = 1
        c = 0
        while r<len(nums):
            if nums[l] > nums[r]:
                c += 1
            l += 1
            r += 1
        if nums[-1] > nums[0]:
            c += 1
        return c<=1
        
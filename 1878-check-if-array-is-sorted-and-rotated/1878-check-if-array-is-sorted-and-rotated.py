class Solution:
    def check(self, nums: List[int]) -> bool:
        l = 0
        r = 1
        c = 0
        while r<len(nums):
            if nums[l]>nums[r]:
                c += 1
            l += 1
            r += 1
        if nums[-1] > nums[0]:
            c+= 1
        return c<=1
        # def issorted(li):
        #     for i in range(1,len(li)):
        #         if li[i-1] > li[i]:
        #             return False
        #     return True
        
        # for i in range(len(nums)):
        #     p = nums.pop()
        #     nums.insert(0,p)
        #     if issorted(nums): return True
        # return False
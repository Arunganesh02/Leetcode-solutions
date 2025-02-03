class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        l = 0 
        r = 1
        mai = 1
        inc = 1
        ind = 1
        mad = 1
        while r<len(nums):
            if nums[l]<nums[r]:
                inc += 1
                mai = max(mai,inc)
                ind = 1
            elif nums[l]>nums[r]:
                ind += 1
                mad = max(mad,ind)
                inc = 1
            else:
                inc = 1
                ind = 1
            l+= 1
            r +=1
        return max(mai,mad)

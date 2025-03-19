class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def bina(tar, lo):
            
            l = 0
            r = len(nums) - 1
            while l<=r:
                mid = ((r-l)//2)+l
                if nums[mid] > tar:
                    r = mid - 1
                else:
                    l = mid + 1
            if l<len(nums) and nums[l] == target and lo:
                return l
            elif r<len(nums) and nums[r] == target and not lo:
                return r
            return -1 
        if len(nums) == 0 : return [-1,-1]
        left = bina(target-0.1, True)
        right = bina(target+0.1 , False)

        return [left , right]
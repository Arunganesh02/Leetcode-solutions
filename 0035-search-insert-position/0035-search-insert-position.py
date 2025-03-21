class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1
        while l<=r:
            mid = ((r-l)//2)+l
            if nums[mid] > target - 0.1:
                r = mid -1
            else:
                l = mid + 1
        return l
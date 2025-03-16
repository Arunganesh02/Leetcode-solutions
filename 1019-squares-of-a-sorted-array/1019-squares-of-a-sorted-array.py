class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        po = len(nums)-1
        l = 0
        r = len(nums)-1
        while l<=r:
            if abs(nums[l]) > nums[r]:
                ans[po] = nums[l]**2
                l += 1
            elif nums[r] > abs(nums[l]):
                ans[po] = nums[r] **2
                r -= 1
            else:
                ans[po] = nums[l]**2
                l+=1
            po -= 1
        return ans 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj1 = c1 = 0
        for i in nums:
            if maj1 == i:
                c1 += 1
            elif c1 == 0 :
                maj1 = i
                c1 += 1
            else: 
                c1 -= 1
        return maj1
        # nums.sort()
        # return nums[len(nums)//2]
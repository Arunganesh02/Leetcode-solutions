class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c0 , c1 , c2 = 0 , 0 , 0 

        for i in nums:
            if i == 0:
                c0 += 1
            elif i == 1: 
                c1+= 1
            elif i == 2: 
                c2 += 1

        p0 , p1 , p2 , = 0 , c0 , c0 + c1

        for i in range(len(nums)):
            if nums[i] == 0:
                nums[p0] , nums[i] = nums[i] , nums[p0]
                p0 += 1

        for i in range(len(nums)):
            if nums[i] == 1:
                nums[p1] , nums[i] = nums[i] , nums[p1]
                p1 += 1
                
        for i in range(len(nums)):
            if nums[i] == 2:
                nums[p2] , nums[i] = nums[i] , nums[p2]
                p2 += 1
        
        return nums
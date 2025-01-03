class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c = 0
        max = 0
        for i in nums:
            if i == 0:
                if c > max:
                    max = c
                c = 0
            else: 
                c+= 1
        if c > max:
            max = c
        
        return max

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        def findlen(n):
            le = 0
            while n>0:
                le += 1
                n //= 10
            return le
        
        c = 0
        for i in range(len(nums)):
            l = findlen(nums[i])
            if l%2 == 0 : c+= 1
        return c
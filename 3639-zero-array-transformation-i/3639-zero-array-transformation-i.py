class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        diff = [0]*(len(nums)+1)
        for i in range(len(queries)):
            st , en  = queries[i]
            diff[st] += 1
            diff[en+1] -= 1


        su = 0 
        for i in range(len(nums)):
            su += diff[i]
            if su < nums[i]:
                return False
        return True
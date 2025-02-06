class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            for j in range(i+1 , len(nums)):
                if nums[i] * nums[j] not in d:
                    d[nums[i] * nums[j]] = 2
                else:
                    d[nums[i] * nums[j]] += 2
        c = 0
        for i in d:
            n = d[i]
            c += n * (n-2)  
        
        return c

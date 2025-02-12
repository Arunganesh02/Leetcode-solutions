class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sumdigits(num):
            ans = 0
            while (num> 0):
                d = num%10
                ans += d
                num //= 10
            return ans
        d = {}
        ma = -1
        for i in nums:
            k = sumdigits(i)
            if k not in d:
                d[k] = i
            else:
                ma = max(ma,d[k]+i)
                d[k] = max(d[k],i)
        return ma
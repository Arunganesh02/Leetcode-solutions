class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        c = 0
        d = {}
        su = 0
        for i in range(len(nums)):
            if i-nums[i] not in d:
                c += su
                d[i-nums[i]] = 1
            else:
                c += su - d[i-nums[i]]
                d[i-nums[i]] += 1
            su += 1
        return c

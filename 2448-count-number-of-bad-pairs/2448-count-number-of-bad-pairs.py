class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        c = 0
        d = {}
        su = 0
        for i in range(len(nums)):
            if nums[i] - i not in d:
                c += su
                d[nums[i] - i] = 1
            else:
                c += su - d[nums[i] - i]
                d[nums[i] - i] += 1
            su += 1
        return c

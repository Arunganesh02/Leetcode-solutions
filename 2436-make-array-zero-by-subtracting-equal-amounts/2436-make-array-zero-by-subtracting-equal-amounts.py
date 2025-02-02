class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        li = sorted(nums)
        op = 0
        recur = 0
        for i in range(len(nums)):
            if li[i] != 0:
                li[i] -= recur
                if li[i] > 0:
                    recur += li[i]
                    op+= 1
        return op

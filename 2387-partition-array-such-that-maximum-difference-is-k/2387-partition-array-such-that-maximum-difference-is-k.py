class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        p1 = 0
        p2 = 1
        subsequences = 0
        mi = float('inf')
        ma = float('-inf')
        while p2<len(nums):
            mi = min(mi , nums[p1] ,nums[p2])
            ma = max(ma , nums[p1] , nums[p2])
            if ma - mi <= k:
                p2+=1
            else:
                subsequences += 1
                p1 = p2
                p2 += 1
                mi = float('inf')
                ma = float('-inf')
        subsequences += 1
        return subsequences
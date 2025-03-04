class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        nums.sort()
        li = [nums[0]]
        for i in range(1 , len(nums)):
            if nums[i][0] <= li[-1][1]:
                li[-1][1] = max(nums[i][1]  , li[-1][1])
            else:
                li.append(nums[i])
        days = 0
        for i in li:
            days += i[1] -(i[0]-1)
        return days
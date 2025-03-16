class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        space = 100000
        nu = 100000
        for i in range(len(nums)):
            k = len(nums) - 1
            j = i+1
            while j<k:
                # for k in range(j+1 , len(nums)):
                su = nums[i] + nums[j] + nums[k]
                close = abs(target - su)
                if abs(nu - target) >close : 
                    space = close
                    nu = su
                if su > target:
                    k -= 1
                elif su < target:
                    j += 1
                else:
                    return nu

        return nu

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i]== nums[i-1]: continue
            k = len(nums)-1
            j = i+1
            while j < k :

                    su = nums[i] + nums[j] + nums[k]
                    if su == 0:
                        ans.append([nums[i] , nums[j] , nums[k]])
                        j += 1
                        while nums[j] == nums[j-1] and j < k :
                            j += 1
                    elif su<0:
                        j += 1
                    else: 
                        k -=1 


        return ans

class Solution:
    def splitArray(self, nums: List[int]) -> int:
        right = [False]*len(nums)
        rightsum = [0]*len(nums)
        su = 0
        bef = -1 
        for i in range(len(nums)-1 , -1 , -1):
            su += nums[i]
            rightsum[i]=su
            if bef == -1 :
                right[i] = True
            else:
                if bef<nums[i] and right[i+1] == True:
                    right[i]= True
                else:
                    right[i] = False
            bef = nums[i]
        leftsum = 0
        ans_minimum = float('inf')
        left_bef = -1
        # print(right , rightsum)
        for i in range(len(nums)-1 ):
            leftsum += nums[i]
            if left_bef == -1 or nums[i] > left_bef:
                if right[i+1] == True:
                    # print(leftsum , rightsum[i+1] , i)
                    ans_minimum = min(abs(leftsum - rightsum[i+1]) , ans_minimum)
            else:
                break    
            left_bef = nums[i]
        if ans_minimum == float("inf"):
            return -1 
        else:
            return ans_minimum


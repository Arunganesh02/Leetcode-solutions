class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        maj = nums[0]
        c = 0 
        for i in range(len(nums)):
            if maj == nums[i]:
                c += 1
            else:
                c -= 1
            if c== 0:
                maj = nums[i]
                c = 1
        k = 0
        indi = -1
        for i in range(len(nums)):
            if nums[i] != maj:
                k += 1
            else:
                k -= 1
            if k == -1:
                indi = i
                break
                
        li = nums[indi+1:]
        c = li.count(maj)

        if c <= len(li)//2:
            return -1

        else: return indi
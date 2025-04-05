class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = []
        def traverse(li ,start):
            if start > len(nums):
                return 
            ans.append(li)
            for i in range(start , len(nums)):
                traverse(li + [nums[i]] ,i+1)
        traverse([] , 0)
        a = 0
        for i in ans:
            tem = 0
            for j in i:
                tem ^= j
            a += tem
        return a
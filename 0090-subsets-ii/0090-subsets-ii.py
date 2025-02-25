class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack ( li , start):
            nonlocal ans , nums
            li.sort()
            if li not in ans:
                ans.append(li)
            for i in range(start , len(nums)):
                backtrack(li+[nums[i]] , i+1)
        backtrack([] , 0)


        return ans
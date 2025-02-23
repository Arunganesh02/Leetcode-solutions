class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def traverse(li , seen ):
            nonlocal n , ans ,nums
            if len(li) == n :
                ans.append(li)
                return 
            for i in range(n):
                if i not in seen:
                    traverse(li+[nums[i]] , seen+[i])
        se = []
        traverse([] , se[:])
        return ans
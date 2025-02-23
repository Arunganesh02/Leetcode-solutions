class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        def traverse(li , seen ):
            nonlocal n , ans ,nums
            if len(li) == n :
                if li not in ans:
                    ans.append(li)
                return 
            for i in range(n):
                if i not in seen:
                    traverse(li+[nums[i]] , seen.union(set([i])))
        traverse([] ,set())
        return ans
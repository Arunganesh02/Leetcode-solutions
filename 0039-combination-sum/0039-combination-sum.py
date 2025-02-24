class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(start , li , sum ,  target ):
            nonlocal ans , candidates 
            if sum == target:
                ans.append(li)
                return 
            elif sum > target:
                return 
            for i in range(start, len(candidates)):
                    backtrack(i ,li+[candidates[i]] , sum + candidates[i] , target)
        backtrack(0,[] , 0 , target)
        return ans
            
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {2:"abc" , 3:"def" , 4: "ghi" , 5:"jkl" , 6:"mno" , 7:"pqrs" , 8:"tuv" , 9:"wxyz"}
        ans = []
        nums = []
        if len(digits) == 0:
            return []
        for i in digits:
            nums.append(d[int(i)])
        def backtrack(li , seen , start):
            nonlocal digits , ans , nums
            
            if len(li) == len(digits):
                ans.append(li)
                return 

            for i in range(start , len(nums)):
                if i not in seen:
                    for j in nums[i]:
                        backtrack(li + j , seen + [i] , i+1)
        backtrack('' , [],0)
        return ans
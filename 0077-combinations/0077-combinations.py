class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def back(li , j):
            nonlocal k,ans , n

            if len(li) == k:
                ans.append(li)
                return 
            for i in range(j+1 , n+1):
                if i not in li:
                    back(li+[i] , i)
            return 
        back([],0)
        return ans
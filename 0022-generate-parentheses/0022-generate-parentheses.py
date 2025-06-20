class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(li , le , ri):

            if le - ri < 0:
                return
                
            if len(li) == n*2:
                if le-ri == 0:
                    ans.append(li)
                return
            
            backtrack(li+"(" ,le+1 , ri)
            backtrack(li+")" ,le ,ri +1)
    
        backtrack("" , 0 , 0)

        return ans
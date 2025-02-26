class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(li):
            nonlocal n , ans
            if len(li) == n*2:
                st = []
                lo = 1
                c1 = 0
                c2 = 0
                for i in li:
                    if i == "(":
                        c1+=1
                    else:
                        c2+=1
                    if i=="(":
                        st.append(i)
                    else:
                        if len(st) != 0 and st[-1] != "(":
                            lo = 0
                            break
                        else:
                            if len(st) != 0:
                                st.pop()
                # print(st)
                if len(st) == 0 and c1==c2==n:
                    ans.append(li)
                return
            
            for i in "()":
                backtrack(li+i)
            
        backtrack("")

        return ans
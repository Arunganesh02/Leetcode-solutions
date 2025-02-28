class Solution:
    def climbStairs(self, n: int) -> int:
        def back(n):
            if n==1 or n==2:
                return se[n]
            else:
                if n not in se:
                    se[n] = back(n-1) + back(n-2)
            return se[n]
        se = {1:1 , 2:2}
        return back(n)
            
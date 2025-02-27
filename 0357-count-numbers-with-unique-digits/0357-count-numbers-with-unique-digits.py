class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = 0
        def backtrack(nu  ,seen):
            nonlocal ans


            if len(str(nu)) > n:
                return
            else:
                if nu and nu[0] != "0":

                    ans += 1

            for i in range (10):
                if i not in seen:

                    backtrack( nu + str(i) , seen + [i])

        backtrack('' ,[])
        return ans+1

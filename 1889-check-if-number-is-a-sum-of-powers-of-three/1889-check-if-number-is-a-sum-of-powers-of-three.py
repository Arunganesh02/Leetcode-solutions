class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        
        nu = n
        while (nu>0):
            rem = nu%3
            if rem > 1:
                return False
            nu //= 3
        return True
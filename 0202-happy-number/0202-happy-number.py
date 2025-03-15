class Solution:
    def isHappy(self, n: int) -> bool:
        if n>1 and n<7:
            return False
        if n>7 and n<10:
            return False
        su = 0
        num = n
        while num>0:
            su += (num%10)**2
            num //=10
        if su == 1:
            return True
        return self.isHappy(su)
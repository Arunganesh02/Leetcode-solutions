class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        score = 0 
        ma = max(a,b,c)
        if ma == a :
            if b+c == a:
                return a
            elif b+c < a:
                return b+c
            else:
                return math.floor((b+c+a)/2) 
        elif ma == b:
            if a+c == b:
                return b
            elif c+a < b:
                return c+a
            else:
                return math.floor((a+c+b)/2) 
        else:
            if b+a == c:
                return c
            elif b+a < c:
                return b+a
            else:
                return math.floor(((b+a)+c) /2) 
            
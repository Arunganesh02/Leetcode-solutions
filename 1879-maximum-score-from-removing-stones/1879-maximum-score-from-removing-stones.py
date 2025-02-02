class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        ma = sorted([a,b,c])
        if ma[-1] == sum(ma[:2]):
            return ma[-1]
        elif sum(ma[:2]) < ma[-1]:
            return sum(ma[:2])
        return math.floor(sum(ma)/2)

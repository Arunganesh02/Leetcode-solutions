class Solution:
    def coloredCells(self, n: int) -> int:
        recur = 0
        ans = 1
        if n == 1:
            return 1
        for i in range(1,n):
            recur += 4
            ans  += recur
        return ans
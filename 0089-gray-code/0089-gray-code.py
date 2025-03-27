class Solution:
    def grayCode(self, n: int) -> List[int]:
        li = ['0','1']
        if n != 1:
            for i in range(n-1):
                k1 = []
                for j in li:
                    k1.append('0'+j)
                k2 = []
                for j in li[::-1]:
                    k2.append('1'+j)
                li = k1 + k2
        ans = []
        for i in li:
            ans.append(int(i,2))
        return ans
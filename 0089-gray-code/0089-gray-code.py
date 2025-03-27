class Solution:
    def grayCode(self, n: int) -> List[int]:
        li = []
        for i in range(2**n):
            li.append(i ^ (i>>1))
        return li
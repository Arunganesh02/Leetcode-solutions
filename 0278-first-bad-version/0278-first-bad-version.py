# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0 
        r = n
        while l<=r:
            mid = ((r-l)//2)+l
            if isBadVersion(mid):
                r = mid -1
            else:
                l = mid +1
        return l
        # for i in range(n+1):
        #     if isBadVersion(i):
        #         return i
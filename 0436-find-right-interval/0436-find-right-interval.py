class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        sor = sorted(intervals)
        d = {}
        # print(sor)
        

        for i in range(len(intervals)):
            d[intervals[i][0]] = i

        def search(target):
            l = 0
            r = len(intervals)-1
            while l<=r:
                mid = ((r-l)//2)+l
                if sor[mid][0] > target-0.1:
                    r = mid - 1
                else:
                    l = mid + 1
            if l>=len(sor):
                return (-1 , False)
            return (sor[l][0] , True)
        ans = []
        for i in range(len(intervals)):
            nu , lo = search(intervals[i][1])
            if lo:
                ans.append(d[nu])
            else:
                ans.append(-1)
        return ans
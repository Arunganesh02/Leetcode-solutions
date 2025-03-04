class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals,key = lambda x:x[0])
        ans = [intervals[0]]

        for i in range( 1, len(intervals)):
            inte = ans[-1]
            if intervals[i][0] in set(range(inte[0] , inte[1]+1)):
                ans[-1][1] = max(inte[1] , intervals[i][1])
            else:
                ans.append(intervals[i])
        
        return ans
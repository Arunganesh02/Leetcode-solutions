class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        ans = [points[0]]
        for i in range(1 , len(points)):
            if ans[-1][1] >= points[i][0]:
                ans[-1][1] = min(ans[-1][1],points[i][1])
            else:
                ans.append(points[i])
        return len(ans)
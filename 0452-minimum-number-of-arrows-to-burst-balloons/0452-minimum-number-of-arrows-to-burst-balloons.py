class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arr = 0
        st = []
        for i in points:
            if len(st) == 0:
                st.append(i)
            elif i[0] <= st[-1][1]:
                arr += 1
                st[-1][1] = min(st[-1][1] , i[1])
            else:
                arr +=1
                st.append(i)
        return len(st)
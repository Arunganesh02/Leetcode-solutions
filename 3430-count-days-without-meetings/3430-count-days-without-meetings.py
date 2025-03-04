class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        li = [meetings[0]]
        for i in range(1 , len(meetings)):
            if  meetings[i][0] <= li[-1][1]:
                li[-1][1] = max(li[-1][1] , meetings[i][1])
            else:
                li.append(meetings[i])
        day = 0
        for i in range(1,len(li)):
            day += li[i][0] - (li[i-1][1]+1) 
        day += li[0][0] - 1
        day += days - li[-1][-1]
        return day
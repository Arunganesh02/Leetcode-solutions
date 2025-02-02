class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        d = {}
        winners = []
        losers = []
        for i in matches:
            if i[0] not in d:
                d[i[0]] = 0
            if i[1] not in d:
                d[i[1]] = 1
            else:
                d[i[1]] += 1
        for i in d:
            if d[i] == 0:
                winners.append(i)
            elif d[i] == 1:
                losers.append(i)
        return [sorted(winners) , sorted(losers)]
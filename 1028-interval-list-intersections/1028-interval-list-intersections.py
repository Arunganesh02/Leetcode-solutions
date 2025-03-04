class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        fp = 0
        sp = 0
        ans = []
        while ( fp<len(firstList) and sp<len(secondList)):
            if secondList[sp][0] <= firstList[fp][1] and secondList[sp][0] >= firstList[fp][0]:
                ans.append([secondList[sp][0], min(firstList[fp][1],secondList[sp][1])])

            elif firstList[fp][0] <= secondList[sp][1] and firstList[fp][0] >= secondList[sp][0]:
                ans.append([firstList[fp][0] , min(secondList[sp][1],firstList[fp][1])])

            if firstList[fp][1] > secondList[sp][1]:
                sp += 1
            else:
                fp += 1
        return ans
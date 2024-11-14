class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        li = sentence.split()
        for i in range(len(li)-1):
            if li[i][-1] != li[i+1][0]:
                return False
        if li[len(li)-1][-1] != li[0][0]:
            return False
        return True
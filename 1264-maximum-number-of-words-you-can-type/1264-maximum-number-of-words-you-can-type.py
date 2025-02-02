class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c = 0
        li = text.split(" ")
        lo = [True]*len(li)
        for i in brokenLetters:
            for j in range(len(li)):
                if i in li[j] and lo[j]:

                    lo[j] = False
        return sum(lo)
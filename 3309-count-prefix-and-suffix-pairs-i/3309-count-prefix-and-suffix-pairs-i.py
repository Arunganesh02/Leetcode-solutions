class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def ispresuf(s1,s2):
            if len(s2) < len(s1):
                return False
            if s1 in s2[:len(s1)] and s1 in s2[len(s2)-len(s1):]:
                return True
            else:
                return False
        c = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if ispresuf(words[i] , words[j]):
                    c += 1
        return c
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c = 0 
        # if len(set(s1)) != len(set(s2)):
        #     return False
        # for i in s2:
        #     if i not in s1:
        #         return False
        if Counter(s1) != Counter(s2):
            return False
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                c+=1
        if c>2:
            return False
        else:
            return True
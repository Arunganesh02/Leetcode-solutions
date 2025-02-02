class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d = {}
        st = s.split(" ")
        if len(st) != len(pattern):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in d:
                d[pattern[i]] = st[i]
            else:
                if d[pattern[i]] != st[i]:
                    return False
        return len(set(d.values())) == len(d) 

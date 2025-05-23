class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {'a': -1, 'b': -1, 'c': -1, 'd': -1, 'e': -1, 'f': -1, 'g': -1, 'h': -1, 'i': -1, 'j': -1, 'k': -1, 'l': -1, 'm': -1, 'n': -1, 'o': -1, 'p': -1, 'q': -1, 'r': -1, 's': -1, 't': -1, 'u': -1, 'v': -1, 'w': -1, 'x': -1, 'y': -1, 'z': -1}
        for i in range(len(s)):
            d[s[i]] = i
        
        r = -1
        ans = []
        st = 0
        for i in range(len(s)):
            if r < d[s[i]]:
                r = d[s[i]]
            if i == r:
                ans.append((r - st)+1)
                st = i+1
                i = r+1
        return ans
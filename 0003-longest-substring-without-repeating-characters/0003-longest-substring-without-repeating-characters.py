class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # ma = 0
        # l = 0
        # h = 0
        # se = set()
        # while l<len(s) and h<len(s):
        #     if l == h:
        #         se.add(s[l])
        #         h += 1
        #     else:
        #         if s[h] not in se:
        #             se.add(s[h])
        #             h += 1
        #         else:
        #             ma = max(ma,len(se))
        #             l += 1
        #             h = l
        #             se = set()
        # ma = max(ma,len(se))
        # return ma



        seen = {}
        l = 0
        length = 0
        for i in range(len(s)):
            if s[i] in seen and seen[s[i]] >= l:
                l = seen[s[i]] + 1
            else:
                length = max(length,i-l +1)
            seen[s[i]] = i

        return length
            
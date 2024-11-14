class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = [s[0]]
        c = 0
        for i in range(1,len(s)):
            if s[i] != stack[-1]:
                stack.append(s[i])
                c = 0
            elif c<1:
                stack.append(s[i])
                c += 1
        return "".join(stack)
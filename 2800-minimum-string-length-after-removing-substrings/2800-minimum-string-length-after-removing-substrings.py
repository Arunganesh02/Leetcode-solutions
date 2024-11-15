class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        if len(s)== 1: return 1
        for i in s:
            if i == "B" and len(stack)!=0 and stack[-1] == "A":
                stack.pop()
            elif i == "D" and len(stack)!=0 and stack[-1] == "C":
                stack.pop()
            else:
                stack.append(i)
        return len(stack)

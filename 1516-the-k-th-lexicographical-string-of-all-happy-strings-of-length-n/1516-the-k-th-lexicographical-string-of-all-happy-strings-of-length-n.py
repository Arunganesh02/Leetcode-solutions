class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        li = []
        def generatechar(n , current):
            nonlocal li
            if len(current) == n:
                li.append(current)
                return 
            for i in ["a","b","c"]:
                if len(current) >0 and current[-1] == i:
                    continue
                generatechar(n , current + i)
        generatechar(n , "")
        if len(li) < k:
            return ""
        else:
            return li[k-1]
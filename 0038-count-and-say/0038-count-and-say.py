class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1 :
            return '1'
        s1='1'
        for i in range(2,n+1):
            s = ''
            c = 0
            t = s1[0]
            for i in range(len(s1)):
                if s1[i] == t:
                    c += 1
                else:
                    s += str(c) + t
                    t = s1[i]
                    c = 1
            s += str(c) + t
            t = s1[i]
            s1 = s
        return s1
            


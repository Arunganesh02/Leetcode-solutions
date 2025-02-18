class Solution:
    def smallestNumber(self, pattern: str) -> str:
        li = ['1']
        counter = 2
        l = 0
        for i in range(len(pattern)):
            if pattern[i] == "D":
                li.insert(l,str(counter))
            else:
                li.append(str(counter))
                l = i+1

            counter+= 1

        return "".join(li)
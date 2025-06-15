class Solution:
    def generateTag(self, caption: str) -> str:

        li = caption.strip().split(" ")
        print(li)

        for i in range(1,len(li)):
            if len(li[i]) != 0:
                li[i] = li[i][0].upper() + li[i][1:].lower()
        print(li)
        if len(li[0]) == 0: return "#"
        li[0] = li[0].lower()
        

        hashtag = "#"+"".join(li)

        return hashtag[:100]
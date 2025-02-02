class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        li = []
        for i in rectangles:
            li.append(min(i))
        ma = max(li)
        return li.count(ma)
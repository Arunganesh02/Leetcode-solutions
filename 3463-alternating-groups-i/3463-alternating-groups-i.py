class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        alt = 0
        for i in range(len(colors)):
            if colors[i-1] != colors[i] and colors[(i+1)%len(colors)] != colors[i]:
                # print(i)
                alt += 1
        return alt
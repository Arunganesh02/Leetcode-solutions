class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        column = []
        for i in range(len(grid)):
            temp = []
            for j in range(len(grid)):
                temp.append(grid[j][i])
            column.append(temp)
        ans = 0
        for i in grid:
            for j in column:
                if i == j :
                    ans += 1
        return ans
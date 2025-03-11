class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxi = 0
        def traverse(i , j ):
            nonlocal su ,maxi
            if grid[i][j] == 0:
                return 
            su += 1
            maxi = max(maxi , su)
            grid[i][j] = 0

            if i+1 < len(grid): traverse(i+1 ,j )
            if i-1 >= 0 : traverse(i-1 ,j)
            if j+1 < len(grid[0]) : traverse(i , j+1)
            if j-1 >=0 : traverse(i , j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    su = 0
                    traverse(i ,j)
        
        return maxi
        

                
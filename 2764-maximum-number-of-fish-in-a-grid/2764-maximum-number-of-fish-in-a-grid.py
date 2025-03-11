class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        maxi = 0 
        
        def traverse(i , j):
            nonlocal maxi , su , seen

            if grid[i][j]==0 or (i,j) in seen:
                return 
            seen.add((i , j))

            su += grid[i][j]
            maxi = max(maxi , su)
            
            if i+1 < len(grid): traverse(i+1 , j)
            if i-1 >-1: traverse(i-1 , j)
            if j+1 <len(grid[0]) : traverse(i , j+1)
            if j-1 >-1 : traverse(i , j-1)

        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] > 0:
                    su = 0
                    traverse(i , j)
                    seen.add((i , j))
                else:
                    seen.add((i , j))
        return maxi
            
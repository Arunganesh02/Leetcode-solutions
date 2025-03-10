class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0 
        def traverse(i ,j):
            nonlocal ans  , grid
            
            if grid[i][j] == "0" :
                return

            grid[i][j] = "0"
            if i+1 < len(grid) :traverse(i+1 , j)
            if i-1 > -1 : traverse(i-1 , j)
            if j+1 < len(grid[0]) : traverse(i , j+1)
            if j-1 > -1 : traverse(i , j-1)

            return 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] =="1":
                    traverse(i , j)

                    ans += 1
        return ans

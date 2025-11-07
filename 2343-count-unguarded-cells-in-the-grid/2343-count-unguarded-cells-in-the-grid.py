class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0 for i in range(n)] for j in range(m)]
        for i in guards:
            grid[i[0]][i[1]] = "G"
        for i in walls:
            print(i)
            grid[i[0]][i[1]] = "W"
        
        def traverse(i ,j , direc):
            nonlocal m , n, grid
            if i<0 or j<0 or j>=n or i>=m:
                return 
            
            if grid[i][j] == "G" or grid[i][j] == "W":
                return
            
            grid[i][j] = "1"
            
            if direc == "down": traverse(i+1,j, direc)
            if direc == "up" : traverse(i-1 , j,direc)
            if direc == "left" : traverse(i , j-1,direc)
            if direc == "right" : traverse(i, j+1 , direc)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "G":
                    traverse(i+1,j,"down")
                    traverse(i-1 , j , "up")
                    traverse(i , j-1, "left")
                    traverse(i, j+1 , "right")
        c = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    c += 1
        print(grid)
        return c
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        ans = 0
        def traverse( i, j , seen , li):
            nonlocal ans , totzero
            if i<0 or j <0 or i >= len(grid) or j >= len(grid[0]) or (i,j) in seen or grid[i][j] == -1: return 
            if grid[i][j] == 2: 
                if li>totzero:
                    ans += 1
                return 
            seen.add((i , j))
            traverse(i , j+1 ,  seen.copy() , li+1)
            traverse(i , j-1 , seen.copy() , li+1)
            traverse(i-1 , j , seen.copy() , li+1)
            traverse(i+1 , j , seen.copy() , li+1)

            
        totzero = 0
        si , sj = 0 , 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    si , sj = i , j
                elif grid[i][j] == 0:
                    totzero +=1
        se = set()
        traverse(si,sj, se , 0)

        return ans
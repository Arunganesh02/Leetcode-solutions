class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        weights = [[float('inf') for i in range(len(grid))] for j in range(len(grid))]
        n = len(grid)
        li = []
        heapq.heapify(li)
        weights[0][0] = 1
        if n==1 : return -1 if grid[0][0] == 1 else 1
        if (grid[0][0] == 0): heapq.heappush(li , [1,[0,0]])
        visited = set()
        while (len(li) != 0):
            wei , node = heapq.heappop(li)
            i,j = node
            if i+1 < n and grid[i+1][j] == 0 and weights[i][j] + 1 < weights[i+1][j] :
                weights[i+1][j] =  weights[i][j] + 1
                heapq.heappush(li , [weights[i][j] + 1 , [i+1,j]])
            if j+1 < n and grid[i][j+1] == 0 and weights[i][j] + 1 < weights[i][j+1] :
                weights[i][j+1] =  weights[i][j] + 1
                heapq.heappush(li , [weights[i][j] + 1 , [i,j+1]]) 
            if i+1 < n  and j+1< n and grid[i+1][j+1] == 0 and weights[i][j] + 1 < weights[i+1][j+1] :
                weights[i+1][j+1] =  weights[i][j] + 1
                heapq.heappush(li , [weights[i][j] + 1 , [i+1,j+1]])
            if i-1 > -1 and grid[i-1][j] == 0 and weights[i][j] + 1 < weights[i-1][j] :
                weights[i-1][j] =  weights[i][j] + 1
                heapq.heappush(li , [weights[i][j] + 1 , [i-1,j]])
            if j-1 > -1 and grid[i][j-1] == 0 and weights[i][j] + 1 < weights[i][j-1] :
                weights[i][j-1] =  weights[i][j] + 1
                heapq.heappush(li , [weights[i][j] + 1 , [i,j-1]])   
            if i-1 > -1  and j+1<n and grid[i-1][j+1] == 0 and weights[i][j] + 1 < weights[i-1][j+1] :
                weights[i-1][j+1] =  weights[i][j] + 1
                heapq.heappush(li , [weights[i][j] + 1 , [i-1,j+1]])
            if i+1 < n  and j-1>-1 and grid[i+1][j-1] == 0 and weights[i][j] + 1 < weights[i+1][j-1] :
                weights[i+1][j-1] =  weights[i][j] + 1
                heapq.heappush(li , [weights[i][j] + 1 , [i+1,j-1]])     
            if i-1 >-1  and j-1>-1 and grid[i-1][j-1] == 0 and weights[i][j] + 1 < weights[i-1][j-1] :
                weights[i-1][j-1] =  weights[i][j] + 1
                heapq.heappush(li , [weights[i][j] + 1 , [i-1,j-1]])                  

        if weights[n-1][n-1] == float("inf") : return -1
        return weights[n-1][n-1]            
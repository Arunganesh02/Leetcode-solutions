class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        mat = [[float('inf') for i in range(n)] for j in range(n)]
        i = j = 0
        while i<n:
            mat[i][j] = 0
            i += 1
            j += 1
        for u,v,w in edges:
            mat[u][v] = w
            mat[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j] = min(mat[i][j]  , mat[i][k] + mat[k][j])

        for i in range(-1 , -(n+1) , -1):
            temp = 0
            for j in range(-1 , -(n+1) , -1):
                if mat[i][j] <= distanceThreshold:
                    temp += 1
            mat[i] = temp
        mi = min(mat)
        for i in range(n-1 , -1 , -1):
            if mat[i] == mi:
                return i
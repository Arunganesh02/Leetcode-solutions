class DisjointSet:
    def __init__(self,n):
        self.size = [1]*(n+1)
        self.parent = [0]*(n+1)
        
        for i in range(n+1):
            self.parent[i] = i
            
    def findupar(self,u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.findupar(self.parent[u])
        return self.parent[u]
        
    def unionBySize(self,u,v):
        parU = self.findupar(u)
        parV = self.findupar(v)
        
        if parU == parV : return
        
        if self.size[parV] > self.size[parU]:
            self.parent[parU] = self.parent[parV]
            self.size[parV] += self.size[parU]
        else:
            self.parent[parV] = self.parent[parU]
            self.size[parU] += self.size[parV]

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        ds = DisjointSet(n-1)
        cable = 0
        for i,j in connections:
            if ds.findupar(i) != ds.findupar(j):
                ds.unionBySize(i,j)
            else:
                cable += 1
        c = 0
        for i in range(n):
           if ds.findupar(i) == i: c += 1

        if cable < (c-1) : return -1
        else: return c-1

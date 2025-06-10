# from typing import List
# import heapq
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
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ds = DisjointSet(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    ds.unionBySize(i , j)
                    # ds.findupar(i)
                    # ds.findupar(j)
            # ds.findupar(i)
        c = 0
        for i in range(len(isConnected)):
            if ds.findupar(i) == i : c+=1 
        return c
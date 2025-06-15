class DisjointSet:
    def __init__(self,n):
        self.size = [1]*(n)
        self.parent = [0]*(n)
        
        for i in range(n):
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        ds = DisjointSet(len(accounts))
        d = {}
        for person in range(len(accounts)):
            for mail in accounts[person][1:]:
                if mail not in d:
                    d[mail] = person
                else:
                    ds.unionBySize(d[mail] , person)
                    d[mail] = person
        ans = {}
        for i in d:
            k = ds.findupar(d[i])
            if k not in ans:    
                ans[k] = [i]
            else:
                ans[k] += [i]
        finalAns = []
        for i in ans:
            ans[i] = sorted(ans[i])
        for i in ans.items():
            finalAns.append([accounts[i[0]][0]] + i[1])
        return finalAns
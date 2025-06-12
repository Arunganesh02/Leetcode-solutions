class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        d = {i:[] for i in range(n)}
        for i,j in connections:
            d[i].append(j)
            d[j].append(i)
        crit = []
        visited = set()
        short  = [0]*n
        react = [0]*n
        count = 0
        def dfs(node , parent):
            nonlocal crit , d , visited , short , react,count
            if node in visited:
                return short[node]
            count +=1 
            react[node] = count
            short[node] = count
            visited.add(node)
            for i in d[node]:
                if i == parent : continue
                if i not in visited:
                    dfs(i , node)
                    short[node] = min(short[node] , short[i])
                    if short[i] > react[node]:
                        crit.append([node , i])
                else:
                    short[node] = min(short[node] , short[i])

        dfs(0,-1)
        return crit
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = {i:[] for i in range(1,n+1)}
        for u,v,w in times:
            if u not in d:
                d[u] = [[v,w]]
            else:
                d[u] += [[v,w]]
        visited  = set()
        weight = [float('inf') for i in range(n+1)]
        weight[k] = 0
        curr = k
        li = [[0,k]]
        heapq.heapify(li)
        while li:
            we , curr = heapq.heappop(li)
            if curr in visited : continue
            visited.add(curr)
            for node,wei in d[curr]:
                if weight[curr] + wei <= weight[node] and node not in visited:
                    weight[node] = weight[curr]+wei
                    heapq.heappush(li , [weight[node] , node])
            
        if max(weight[1:]) == float('inf'):
            return -1
        return max(weight[1:])
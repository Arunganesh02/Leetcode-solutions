class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # d = {i:[] for i in range(n)}
        # for u,v,w in flights:
        #     d[u] += [[v,w]]

        # visited = set()
        # weights = [float('inf') for i in range(n)]
        # bef = [0 for i in range(n)]
        # weights[src] = 0
        # li = [[0,src]]
        # heapq.heapify(li)

        # while li:
        #     we , curr = heapq.heappop(li)
        #     if curr in visited:
        #         continue
        #     visited.add(curr)


        #     for node , weight in d[curr]:
        #         if weights[curr] + weight <= weights[node] and node not in visited and bef[curr] <=k:
        #             weights[node] = weights[curr] + weight
        #             heapq.heappush(li ,[weights[node] , node])
        #             bef[node] = bef[curr]+1
        # print(weights)
        # if weights[dst] == float('inf') : return -1
        # return weights[dst]
        

        dist = [float('inf') for i in range(n)]
        dist[src] = 0

        for i in range(k+1):
            temp = dist.copy()

            for u,v,w in flights:
                if dist[u] == float("inf"):
                    continue
                if dist[u] + w <= temp[v] :
                    temp[v] = dist[u] + w
            dist = temp

        return -1 if dist[dst] == float('inf') else dist[dst]

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        d = {i:[] for i in range(len(graph))}
        st = []
        visited = set()
        for i in range(len(graph)):
            for j in graph[i]:
                d[j] += [i]
        
        indeg = [0 for i in range(len(graph))]
        for i in d:
            for j in d[i]:
                indeg[j] += 1 
        queue = []
        for i in range(len(indeg)):
            if indeg[i] == 0:
                queue.append(i)
        st=[]
        while (len(queue) != 0):
            p = queue.pop(0)
            st.append(p)
            
            for i in d[p]:
                indeg[i] -= 1
                if indeg[i] == 0: queue.append(i)
        st.sort()
        return st

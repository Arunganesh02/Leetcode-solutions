class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = {i:[] for i in range(numCourses)}
        st = []
        for u,v in prerequisites:
            d[v] += [u]
        indeg = [0 for i in range(numCourses)]
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
        if (len(st) != numCourses): return []
        return st

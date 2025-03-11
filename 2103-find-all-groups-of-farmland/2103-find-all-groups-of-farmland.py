class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        ans = []

        def traverse(i , j):
            nonlocal ei , ej
            if land[i][j] == 0:
                return 
            
            land[i][j] = 0
            ei , ej = max(ei , i) , max(ej , j)
            if i+1 < len(land): traverse(i+1 , j)
            if j+1 < len(land[0]): traverse(i , j+1)

            
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == 1 : 
                    ei , ej = 0,0
                    traverse(i , j)
                    ans.append([i , j,ei,ej])
        
        return ans
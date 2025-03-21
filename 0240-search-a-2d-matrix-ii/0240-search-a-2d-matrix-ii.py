class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0 
        r = len(matrix)-1
        def binary(li):
            ll = 0
            rr = len(li)-1
            while ll <= rr:
                mid = ((rr - ll)//2)+ll
                
                if li[mid] == target:
                    return True
                elif li[mid] > target:
                    rr = mid -1
                else:
                    ll = mid +1
            return False
        for i in range(len(matrix)):
            if binary(matrix[i]):
                return True
        return False
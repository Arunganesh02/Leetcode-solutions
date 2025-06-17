class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)  < 3: return False
        inc = False
        dec = False
        ini = arr[0]
        bre = len(arr)- 1
        for i in range(1 , len(arr)):
            if ini < arr[i]:
                inc = True
                ini = arr[i]
            else:
                bre = i
                break
        for i in range(bre , len(arr)):
            if ini > arr[i]:
                dec = True
            else:
                dec = False
                break
            ini = arr[i]
        return inc and dec
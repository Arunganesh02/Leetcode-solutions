class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lo = [True]*len(flowerbed)
        k = 0
        for i in range(len(flowerbed)):

            if flowerbed[i] == 1 and lo[i]:
                lo[i] = False
                if i-1 != -1:
                    lo[i-1] = False
                if i+1 != len(flowerbed):
                    lo[i+1] = False

            elif flowerbed[i] == 0 and lo[i]:

                if i+1 == len(flowerbed) or flowerbed[i+1] != 1:
                    k+= 1
                    if i+1 < len(flowerbed):
                        lo[i+1] = False
                lo[i] = False
                    
        # print(lo , k)
        return k >= n


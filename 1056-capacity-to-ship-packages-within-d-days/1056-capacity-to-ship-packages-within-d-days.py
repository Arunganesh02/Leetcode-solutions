class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # def search(capacity):
        #     day = 1
        #     temp = 0
        #     j = 0
        #     while j<len(weights):
        #         if temp+weights[j]  > capacity:
        #             day += 1
        #             temp = weights[j]
        #         else:
        #             temp += weights[j]
        #         j+=1
        #     return day


        # l = max(weights)
        # r = sum(weights)
        # while l<=r:
        #     mid = l+((r-l)//2)
        #     day = search(mid)
        #     if day < days:
        #         r = mid -1
        #     elif day > days:
        #         l = mid +1
        #     else:
        #         r = mid -1
        # return l


        def search(da):
            su = 0
            ans = 0
            for i in range(len(weights)):
                if su+weights[i] > da:
                    ans += 1
                    su = 0
                su += weights[i]
            ans += 1
            return ans

        l = max(weights) 
        r = sum(weights)

        while l<=r:
            mid = ((r-l)//2)+l
            if search(mid) <= days:
                r = mid - 1
            else:
                l = mid + 1
        return l            
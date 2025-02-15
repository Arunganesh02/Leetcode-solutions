class Solution:
    def punishmentNumber(self, n: int) -> int:
        def sumofdigits(num , target):
            if not num and target == 0:
                return True
            if target< 0:
                return False
            
            for i in range(len(num)):
                left = num[:i+1]
                right = num[i+1:]
                left = int(left)

                if sumofdigits(right , target - left):
                    return True
            return False
        ans = 0
        # print(sumofdigits(1))
        for i in range(1 , n+1):
            if sumofdigits(str(i*i) , i) :
                print(i)
                ans += i*i
        return ans
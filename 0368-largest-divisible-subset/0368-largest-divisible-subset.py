class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        ans = []
        nums.sort()
        def traverse(i , j ):
            nonlocal ans
            # if len(li) > len(ans):
            #     ans = li
            if i == -1: return 0
            take = 0
            if j ==-1 or nums[j]%nums[i] == 0 or nums[i]%nums[j]== 0:
                take = 1 +traverse(i-1 , i )
            nottake = traverse(i-1 , j )

            return max(take , nottake)
        ahead = [0 for j in range(len(nums)+1)]
        now = [0 for j in range(len(nums)+1)]

        maxi = 0
        hashing = [-1 for i in range(len(nums))]
        indi = -1
        for i in range(len(nums)):
            for j in range(i):
                if nums[j]%nums[i] == 0 or nums[i]%nums[j]== 0:
                    if now[i]<now[j]+1:
                        now[i] =  now[j] + 1
                        hashing[i] = j
            # maxi = max(maxi , now[i])
            if now[i] > maxi:
                indi = i
                maxi = now[i]
        li = []       
        k = hashing[indi]
        li.append(nums[indi])
        while k != -1:
            li.append(nums[k])
            k = hashing[k]
        li.reverse()
        return li
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        op = 0
        while (True):
            p = nums[0]
            if ( p >= k or len(nums) == 1):
                break
            sm1 = heapq.heappop(nums)
            sm2 = heapq.heappop(nums)
            heapq.heappush(nums , (min(sm1 , sm2) * 2)+max(sm1,sm2))
            op += 1
        return op
        
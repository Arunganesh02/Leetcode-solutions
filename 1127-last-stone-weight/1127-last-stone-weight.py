import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq._heapify_max(stones)
        while(len(stones)>1  ):
            y = heapq.heappop(stones)
            heapq._heapify_max(stones)
            x = heapq.heappop(stones)
            if (x != y):
                heapq.heappush(stones , y-x)
            heapq._heapify_max(stones)
        if len(stones) == 1: return stones[0]
        return 0
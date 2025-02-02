class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        greedy = []
        for i in range(len(capacity)):
            greedy.append(capacity[i] - rocks[i])
        greedy = sorted(greedy)
        for i in range(len(greedy)):
            if greedy[i] != 0:
                if additionalRocks>=greedy[i]:
                    additionalRocks -= greedy[i]
                    greedy[i] = 0 
                else:
                    break
        c = 0
        for i in range(len(greedy)):
            if greedy[i]==0:
                c += 1
            else:
                break
        return c

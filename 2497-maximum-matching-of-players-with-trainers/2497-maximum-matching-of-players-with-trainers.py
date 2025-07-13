class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players = sorted(players, reverse = True)
        trainers = sorted(trainers, reverse = True)
        i,j= 0,0
        ans = 0
        # print(players , trainers)
        while i<len(players) and j<len(trainers):
            if players[i] <= trainers[j]:
                ans += 1
                j+=1
            i+=1
        return ans
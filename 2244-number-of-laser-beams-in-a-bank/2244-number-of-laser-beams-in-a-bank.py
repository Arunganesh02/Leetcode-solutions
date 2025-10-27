class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        que = []
        beams = 0
        for i in range(-1 ,-(len(bank)+1) , -1):
            ones = bank[i].count("1")
            if ones == 0 : continue
            if len(que)!=0:
                beams += (ones * que[-1])
                que.pop()
                que.append(ones)
            else:
                que.append(ones)
        return beams
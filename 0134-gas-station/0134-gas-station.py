class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # ind = 0
        # li = []
        # if len(gas) ==1 :
        #     if gas[0] >= cost[0]: return 0
        #     else: return -1
        # for i in range(len(gas)):
        #     if gas[i]>cost[i]:
        #         li.append(i)
                
        # for ind in li:
        #     vis = set()
        #     bal = 0
        #     ans = ind
        #     while True:
        #         if ind in vis:
        #             return ans
        #         bal += gas[ind]
        #         bal  -= cost[ind]
        #         # print(bal , ind)
        #         if bal < 0:
        #             break
        #         vis.add(ind)
        #         if ind ==len(gas)-1:
        #             ind =0
        #         else: ind += 1
        #     # else:  
        #     #     return ans
        # return -1

        if sum(gas) < sum(cost):
            return -1

        st = 0
        su = 0
        for i in range(len(gas)):
            su += gas[i] - cost[i]
            if su <0:
                st = i + 1
                su = 0
        return st
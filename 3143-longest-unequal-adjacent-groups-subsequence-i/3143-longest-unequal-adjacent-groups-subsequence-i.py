class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        # def traverse(indi , li):
        #     if indi == 0 : 
        #         li.append(words[indi])
        #         return li
        #     take = []
        #     if dp[indi] != -1 : return dp[indi]
        #     if groups[indi-1] != groups[indi]:
        #         take = traverse(indi-1 , li + [words[indi]])
        #     nottake = traverse(indi-1 , li)
        #     if len(take)>len(nottake): 
        #         dp[indi] = take
        #         return take
        #     else: 
        #         dp[indi] = nottake
        #         return nottake

        # dp = [-1 for i in range(len(words)+1)]
    
        # return traverse(len(words)-1 , [])[::-1]

        last = groups[0]
        li = [words[0]]
        for i in range(1 , len(words)):
            if groups[i]!=last:
                last = groups[i]
                li.append(words[i])
        return li
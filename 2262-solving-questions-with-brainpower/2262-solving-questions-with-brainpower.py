class Solution(object):
    def mostPoints(self, questions):
        def traverse(start):
            if start >=len(questions) : return 0
            if dp[start] != -1 : return dp[start]
            take = questions[start][0] + traverse(start+questions[start][1]+1)
            leave = traverse(start+1)
            dp[start] = max(take , leave)
            return dp[start]

        dp = [-1]* len(questions)
        return traverse(0)
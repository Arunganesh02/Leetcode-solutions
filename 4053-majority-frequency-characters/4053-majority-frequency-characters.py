class Solution:
    def majorityFrequencyGroup(self, s: str) -> str:
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        dc = {}
        for i in d:
            if d[i] not in dc:
                dc[d[i]] = i
            else:
                dc[d[i]] += i
        max_str = ''
        max_cnt = 0

        for i in dc:
            if len(dc[i]) == len(max_str):
                if i > max_cnt:
                    max_cnt = i
                    max_str = dc[i]
            if len(dc[i]) > len(max_str):
                max_cnt = i
                max_str = dc[i]
        return max_str
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = {}
        li = []
        ti = math.floor(len(nums)/3)
        print(ti)
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in d:
            if d[i] > ti:
                li.append(i)
        return li
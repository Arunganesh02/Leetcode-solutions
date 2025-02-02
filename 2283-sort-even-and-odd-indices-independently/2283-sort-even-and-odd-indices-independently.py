class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd = []
        even = []
        li = []
        for i in range(len(nums)):
            if i%2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort()
        even.sort()
        for i in range(len(nums)):
            if i%2 == 1:
                p = odd.pop()
                nums[i] = p
            else:
                p = even.pop(0)
                nums[i] = p
        return nums

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0 
        r = len(letters)-1
        while l<=r:
            mid = ((r-l)//2)+l
            # if ord(letters[mid]) == ord(target):
            #     if mid+1 < len(letters):
            #         return letters[mid+1]
            #     return letters[0]
            if ord(letters[mid]) > ord(target):
                r = mid -1
            else: 
                l = mid + 1
        if l>=len(letters):
            return letters[0]
        return letters[l]

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height)-1
        maximum_water = float('-inf')
        while left<right:
            maximum_water = max(maximum_water , min(height[left] , height[right]) * (right - left))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return maximum_water
            
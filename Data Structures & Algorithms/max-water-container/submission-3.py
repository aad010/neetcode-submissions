class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0 
        right = len(heights) - 1
        maxVal = 0

        while left < right: 
            print(heights[left], heights[right], min(heights[left], heights[right]))
            height_val = min(heights[left], heights[right])
            maxVal = max(maxVal, (height_val * (right - left)))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return maxVal

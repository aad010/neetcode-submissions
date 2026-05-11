class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i = 0
        j = len(heights) - 1
        maxContainer = 0
        while i < j:
            maxContainer = max(maxContainer, (j - i) * min(heights[i],heights[j]))
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return maxContainer
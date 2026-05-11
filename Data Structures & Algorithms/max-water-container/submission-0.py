class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
            Problem: Given int arr (heights) => heights[i] = height of ith bar
            Goal: chose any two bars to form a container and return max amt of water a container
            can store

            understand example:
            input: 1,7,2,5,4,7,3,6
                     l  r
            max = 36 (6 * 6 = 36)
            work thru it 
            output: 36

            i: 2,2,2
               l r
        '''
        maxHeight = 0
        leftPtr = 0
        rightPtr = len(heights) - 1

        while leftPtr < rightPtr: 
            currHeight = (rightPtr - leftPtr) * min(heights[leftPtr], heights[rightPtr])

            if heights[leftPtr] < heights[rightPtr]:
                leftPtr += 1
            else:
                rightPtr -= 1
            maxHeight = max(currHeight, maxHeight)
    
        return maxHeight
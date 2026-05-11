class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
            given grid where grid[i] is either a 0 (representing water)
            or 1 (representing land)

            area is defined as number of cells within island
            return maximum area of an island in grid

        '''
        maxArea = 0

        def dfs(row, col):
            rows, cols = len(grid), len(grid[0])
            if min(row, col) < 0 or row == rows or col == cols or grid[row][col] == 0:
                return 0 
            count = 1
            grid[row][col] = 0
            count += dfs(row - 1, col)
            count += dfs(row + 1, col)
            count += dfs(row, col - 1)
            count += dfs(row, col + 1)
            return count
            
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, (dfs(row,col)))
                
        return maxArea

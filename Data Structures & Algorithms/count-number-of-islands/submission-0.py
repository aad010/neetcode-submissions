class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
            given 2D grid where '1' reps land and '0'
            reps water, count & return # of islands
        '''
        visited = set()
        def dfs(x,y):
            rows, columns = len(grid), len(grid[0])
            if (min(x,y) < 0 or (x,y) in visited or x == rows or y == columns or grid[x][y] == "0"):
                return 0
            visited.add((x,y))
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return 1
        
        count = 0
        for value in range(len(grid)):
            for col in range(len(grid[0])):
                count += dfs(value,col)

        return count
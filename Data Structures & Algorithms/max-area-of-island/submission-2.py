class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if (r < 0) or (r == rows) or (c < 0) or (c == cols) or (grid[r][c] == 0):
                return 0
            else:
                grid[r][c] = 0
                val = 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)
                return val

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    val = dfs(r, c)
                    area = max(area, val)

        return area
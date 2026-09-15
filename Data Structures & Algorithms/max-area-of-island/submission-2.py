class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0
        
        res = 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        def dfs(r,c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visited or grid[r][c]== 0:
                return 0

            visited.add((r,c))
            return (1 + dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1))

        area = 0
        for row in range(rows):
            for col in range(cols):
                area = max(area, dfs(row, col))
        return area
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        self.res = 0

        rows, cols = len(grid), len(grid[0])

        def dfs(i,j):
            if i < 0 or i >= rows or j < 0 or j >= cols or (i,j) in visited or grid[i][j] == 0:
                return 0
            

            visited.add((i,j))
            area = 1
            directions = [[1,0],[-1,0],[0,1],[0,-1]]

            for dr, dc in directions:
                area += dfs(i+dr, j+dc)
            return area
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    self.res = max(self.res,dfs(row,col))
        return self.res

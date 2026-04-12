class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        res = 0
        def dfs(r, c):

            if r < 0 or c < 0 or c >= cols or r >= rows or (r,c) in visited or grid[r][c] == '0':
                return

            
            visited.add((r,c))

            dirs = [[0,1], [1,0], [-1,0], [0,-1]]



            for dx, dy in dirs:
                dfs(r+dx, c+dy)
            

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1' and (row,col) not in visited:
                    dfs(row,col)
                    res += 1
        return res
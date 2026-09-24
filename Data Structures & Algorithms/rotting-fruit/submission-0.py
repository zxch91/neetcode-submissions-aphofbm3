class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()
        fresh = 0
        
        rows, cols = len(grid), len(grid[0])

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh += 1
                if grid[row][col] == 2:
                    q.append((row,col,0))

        time = 0
        dirs = [[1,0],[-1,0],[0,1],[0,-1]]
        while q:
            currRow, currCol, time = q.popleft()

            for dr, dc in dirs:
                nr, nc = currRow + dr, currCol + dc

                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    q.append((nr, nc, time + 1))
                    grid[nr][nc] = 2
                    fresh -= 1
                    
        if fresh == 0:
            return time
        else:
            return -1
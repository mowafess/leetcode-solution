class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRS = {(0, 1), (1, 0), (-1, 0), (0, -1)}

        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(r, c):
            if (0 > r or r >= m or 0 > c or c >= n) or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"

            for dr, dc in DIRS:
                dfs(r + dr, c + dc)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    dfs(r, c)
                    count += 1
        
        return count
        
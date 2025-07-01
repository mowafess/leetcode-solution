class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0

        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        pos = ((-1, 0), (1, 0), (0, -1), (0, 1))

        def dfs(r, c):
            if not grid[r][c]:
                return 0
            
            area = grid[r][c]
            grid[r][c] = 0

            for dr, dc in pos:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc]:
                    area += dfs(nr, nc)
            
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r, c)
                    max_area = max(max_area, area)
        
        return max_area
        
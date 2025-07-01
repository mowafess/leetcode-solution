class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid or not grid[0]:
            return 0

        pos = {(-1, 0), (0, 1), (0, -1), (1, 0)}

        total = 0
        rows = len(grid)
        cols = len(grid[0])

        is_within = lambda x, limit: 0 <= x < limit

        def dfs(r, c):
            if grid[r][c] == '0':
                return
            
            grid[r][c] = '0'

            for dr, dc in pos:
                nr, nc = r + dr, c + dc
                if is_within(nr, rows) and is_within(nc, cols) and grid[nr][nc] == '1':
                    dfs(nr, nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    total += 1

        return total
        
    def bfs(self, grid, r, c, pos, rows, cols):
        is_within = lambda x, limit: 0 <= x < limit

        q = collections.deque([(r, c)])

        while q:
            r, c = q.popleft()
            for dr, dc in pos:
                nr, nc = r + dr, c + dc
                if is_within(nr, rows) and is_within(nc, cols) and grid[nr][nc] == '1':
                    q.append((nr, nc))
                    grid[nr][nc] = '0'
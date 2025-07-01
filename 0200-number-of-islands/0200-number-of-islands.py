class Solution:
    pos = {(0, -1), (0, 1), (1, 0), (-1, 0)}

    def numIslands(self, grid: List[List[str]]) -> int:


                # bfs
        queue = deque([])
        xlim = len(grid)
        ylim = len(grid[0])
        count = 0
        
        for x in range(xlim):
            for y in range(ylim):
                if grid[x][y] == '1':
                    grid[x][y] = '0'
                    queue.append((x, y))
                    self.bfs(grid, queue, xlim, ylim)
                    count += 1

        return count

    def bfs(self, grid: List[List[str]], queue: Deque[tuple[int]], xlim: int, ylim: int):
        isWithinbound = lambda grid, x, y, xlim, ylim: \
            0 <= x < xlim and 0 <= y < ylim and grid[x][y] == '1'
        while queue:
            x, y = queue.popleft()
            for del_x, del_y in self.pos:
                new_x, new_y = x + del_x, y + del_y
                if isWithinbound(grid, new_x, new_y, xlim, ylim):
                    queue.append((new_x, new_y))
                    grid[new_x][new_y] = '0'

        # def dfs(r, c):
        #     if grid[r][c] == "0":
        #         return 
        #     grid[r][c] = "0"

        #     for dr, dc in dirs:
        #         nr = r + dr
        #         nc = c + dc
        #         if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
        #             dfs(nr, nc)

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1":
        #             dfs(r, c)
        #             total += 1

        # return total
        
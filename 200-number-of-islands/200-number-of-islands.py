from collections import deque
from typing import List, Deque

class Solution:
    pos = {(0, -1), (0, 1), (1, 0), (-1, 0)}

    def numIslands(self, grid: List[List[str]]) -> int:
        
        if not grid or not grid[0]:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        count = 0
        
        def isOutOfBound(r, c):
            return r < 0 or c < 0 or r >= ROWS or c >= COLS 
        
        def dfs(r, c):
            if isOutOfBound(r, c) or grid[r][c] == "0":
                return
            grid[r][c] = "0" 
            for dr, dc in self.pos:
                dfs(r + dr, c + dc)
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
          
        return count
        
        
        
        # bfs
#         queue = deque([])
#         xlim = len(grid)
#         ylim = len(grid[0])
#         count = 0
        
#         for x in range(xlim):
#             for y in range(ylim):
#                 if grid[x][y] == '1':
#                     grid[x][y] = '0'
#                     queue.append((x, y))
#                     self.bfs(grid, queue, xlim, ylim)
#                     count += 1

#         return count

#     def bfs(self, grid: List[List[str]], queue: Deque[tuple[int]], xlim: int, ylim: int):
#         isWithinbound = lambda grid, x, y, xlim, ylim: \
#             0 <= x < xlim and 0 <= y < ylim and grid[x][y] == '1'
#         while queue:
#             x, y = queue.popleft()
#             for del_x, del_y in self.pos:
#                 new_x, new_y = x + del_x, y + del_y
#                 if isWithinbound(grid, new_x, new_y, xlim, ylim):
#                     queue.append((new_x, new_y))
#                     grid[new_x][new_y] = '0'
from collections import deque

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        directions = {(-1, 0), (1, 0), (0 , 1), (0, -1)}

        rows = len(grid)
        cols = len(grid[0])
        

        def bfs(r, c):
            visited = set()
            q = deque([(r, c)])
            total = 0

            while q:
                r, c = q.popleft()

                if (r, c) in visited:
                    continue
                
                total += 4
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and  0 <= nc < cols and grid[nr][nc]:
                        total -= 1
                        q.append((nr, nc))
                
                visited.add((r, c))
            
            return total

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return bfs(r, c)
        
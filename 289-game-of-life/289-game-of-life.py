class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        positions = set()
        directions = {(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)}
        R, C = len(board), len(board[0])
        
        def countNeighbours(i, j):
            total = 0
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < R and 0 <= nj < C and board[ni][nj]:
                    total += 1
            return total
        
        for i in range(R):
            for j in range(C):
                isAlive = bool(board[i][j])
                neighbours = countNeighbours(i, j)
                if (isAlive and (neighbours < 2 or neighbours > 3)) or (not isAlive and neighbours == 3):
                    positions.add((i, j))
        
        for i, j in positions:
            board[i][j] ^= 1
                    
        
        
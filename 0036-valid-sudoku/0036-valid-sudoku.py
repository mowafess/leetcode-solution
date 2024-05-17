class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)
        
        board_size = len(board)
        sqr_size = 3
        
        for row in range(board_size):
            for col in range(board_size):
                val = board[row][col]
            
                if val != '.':
                    sqr = (row//sqr_size, col//sqr_size)

                    if val in rows[row] or val in cols[col] or val in sqrs[sqr]:
                        return False

                    rows[row].add(val)
                    cols[col].add(val)
                    sqrs[sqr].add(val)
                
        return True
        
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = defaultdict(set)
        cols = defaultdict(set)
        sqrs = defaultdict(set)
        
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                
                if val == '.':
                    continue
                
                sqr = (row//3) *  3 + col//3
                if val in rows[row] or val in cols[col] or val in sqrs[sqr]:
                    return False
                rows[row].add(val)
                cols[col].add(val)
                sqrs[sqr].add(val)
                
        return True
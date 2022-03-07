class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        R, C = len(matrix), len(matrix[0])
        cols, rows = set(), set()
        
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        def zeroFill(rows, cols):
            for i in rows:
                for j in cols:
                    matrix[i][j] = 0
                
        
        zeroFill(rows, range(C))
        zeroFill(range(R), cols)
                    
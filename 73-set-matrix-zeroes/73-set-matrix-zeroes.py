class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        R, C = len(matrix), len(matrix[0])
        positions = {"cols": set(), "rows": set()}
        
        for i in range(R):
            for j in range(C):
                if matrix[i][j] == 0:
                    positions["cols"].add(j)
                    positions["rows"].add(i)
        
        def zeroFill(rows, cols):
            for i in rows:
                for j in cols:
                    matrix[i][j] = 0
                
        
        zeroFill(positions["rows"], range(C))
        zeroFill(range(R), positions["cols"])
                    
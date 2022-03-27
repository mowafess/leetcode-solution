class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0: 
            return False
        
        # start from top right, could also start from bottom left
        r, c = 0, len(matrix[0]) - 1 
        
        while True:
            if r < 0 or c < 0 or r >= len(matrix): 
                return False
            
            if matrix[r][c] == target: 
                return  True
            
            if matrix[r][c] > target: 
                c -= 1
            else: 
                r += 1
        
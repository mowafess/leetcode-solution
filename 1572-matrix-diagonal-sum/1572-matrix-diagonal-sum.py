class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        
        n = len(mat)
        total = 0
        
        for i in range(n):
            total += mat[i][i]
            total += mat[~i][i]
            
            if n%2 == 1 and i == n//2:
                total -= mat[i][i]
            
        return total
        
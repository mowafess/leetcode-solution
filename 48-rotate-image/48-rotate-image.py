class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        3 2 1
        6 5 4
        9 8 7
        """
        k = len(matrix)
        for i in range(k):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
            for j in range(k // 2):
                matrix[i][j], matrix[i][~j] = matrix[i][~j], matrix[i][j]
            
                

        
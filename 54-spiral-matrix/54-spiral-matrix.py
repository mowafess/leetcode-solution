class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        
        top, left, right, bottom = 0, 0, len(matrix[0]), len(matrix)
        
        while top < bottom and left < right:
            col = left
            while col < right:
                res.append(matrix[top][col])
                col += 1
            top += 1
            
            row = top
            while row < bottom:
                res.append(matrix[row][right-1])
                row += 1
            right -= 1
            
            if not(left < right and top < bottom): 
                break
            
            col = right
            while col > left:
                res.append(matrix[bottom-1][col-1])
                col -= 1
            bottom -= 1
            
            row = bottom
            while row > top:
                res.append(matrix[row-1][left])
                row -= 1
            left += 1
            
        return res
            
        

        
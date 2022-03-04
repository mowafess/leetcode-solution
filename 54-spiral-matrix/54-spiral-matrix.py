class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        res = []
        
        top, left, right, bottom = 0, 0, len(matrix[0]), len(matrix)
        0, 0, 3, 3
        
        while top < bottom and left < right:
            col = left
            while col < right:
                res.append(matrix[top][col])
                col += 1
            top += 1
            print(1, res)
            
            row = top
            while row < bottom:
                res.append(matrix[row][right-1])
                row += 1
            right -= 1
            print(2, res)
            
            if not(left < right and top < bottom): break
            
            col = right
            while col > left:
                res.append(matrix[bottom-1][col-1])
                col -= 1
            bottom -= 1
            print(3, res)
            
            row = bottom
            while row > top:
                res.append(matrix[row-1][left])
                row -= 1
            left += 1
            print(4, res)
            
        return res
            
        

        
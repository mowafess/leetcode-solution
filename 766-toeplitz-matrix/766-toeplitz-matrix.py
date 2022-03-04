class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        groups = {}
        
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        
        return True
        
        
        
#         R = len(matrix)
#         C = len(matrix[0])
        
#         def extractDiagonal(r, c):            
#             res = []
#             while 0 <= r < R and 0 <= c < C:
#                 res.append(matrix[r][c])
#                 r += 1
#                 c += 1
#             return res
        
#         def isSameValue(first, arr):
#             return all(x == first for x in arr)
        
#         c = 0
#         for r in range(R):
#             if not isSameValue(matrix[r][c], extractDiagonal(r, c)):
#                 return False
            
#         r = 0
#         for c in range(C):
#             if not isSameValue(matrix[r][c], extractDiagonal(r, c)):
#                 return False
        
#         return True
        
            
                
        
        
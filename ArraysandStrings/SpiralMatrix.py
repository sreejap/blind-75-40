#https://leetcode.com/problems/spiral-matrix/description/
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # boundaries
        # left = 0, right = cols-1, down = 0, up = rows - 1
        # left + and must be less than cols, right - and must be > 0
        # down + , must be less than rows, up - must be > 0

        # we can have while loop for total cells m*n

        # i < m*n
        # dirs = 0,1,2,3
        # if 0 - increase c in the same r until right, then increement dir
        # if 1 - increase r in the same c until bottomw, then inc dir
        # if 2 - decreaase c in the same r until left, then inc dir
        # if 3 - deccrease r in the same c until top, then in dir 
        # dir = dir%4

        
        rows = len (matrix) # 3
        cols = len (matrix[0]) # 3
        res = []
        dirs = 0
        left = 0
        right = cols-1 # 2
        bottom = rows-1 # 2
        top = 0

        if not matrix or not matrix [0]:
            return []

        while left <= right and top <= bottom:
            if dirs == 0:
                for c in range (left,right+1):
                    res.append(matrix[top][c])
                dirs += 1
                top += 1
             elif dirs == 1:
                for r in range (top,bottom+1):
                    res.append (matrix[r][right])
                dirs += 1
                right -= 1
            elif dirs == 2:
                for c in range (right,left-1,-1):
                    res.append (matrix[bottom][c])
                dirs += 1
                bottom -= 1            
            elif dirs == 3:
                for r in range (bottom,top-1,-1):
                    res.append (matrix[r][left])
                dirs += 1
                left += 1
            dirs = dirs %4
        return res        

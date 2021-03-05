# 54. Spiral Matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        result = [0] * m * n
        direction = 0
        
        j = 0
        while top <= bottom and left <= right:
            # 0 -> move right
            if direction == 0:
                for i in range(left, right + 1):
                    result[j] = matrix[top][i]
                    j += 1
                top += 1
            # 1 -> move down
            elif direction == 1:
                for i in range(top, bottom + 1):
                    result[j] = matrix[i][right]
                    j += 1
                right -= 1
            # 2 -> move left
            elif direction == 2:
                for i in range(right, left - 1, -1):
                    result[j] = matrix[bottom][i]
                    j += 1
                bottom -= 1
            # 3 -> move up
            elif direction == 3:
                for i in range(bottom, top - 1, -1):
                    result[j] = matrix[i][left]
                    j += 1
                left += 1
                    
            direction = (direction + 1) % 4
        
        return result

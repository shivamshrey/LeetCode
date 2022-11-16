# 85. Maximal Rectangle
# https://leetcode.com/problems/maximal-rectangle/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        result = 0
        stack = [-1]    # monotonically increasing stack
        
        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                # stack top will be the limiting height
                h = heights[stack.pop()]
                w = (i - 1) - stack[-1]
                result = max(result, h * w)
            stack.append(i)
    
        return result
    
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        result = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = int(matrix[i][j])
                if i != 0:
                    if matrix[i][j] != 0:
                        matrix[i][j] += matrix[i - 1][j]
            result = max(result, self.largestRectangleArea(matrix[i]))
        
        return result        
    
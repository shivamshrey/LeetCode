# 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/

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
    
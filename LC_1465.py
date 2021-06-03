# 1465. Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()
        
        max_h = max(horizontalCuts[0], h - horizontalCuts[-1])
        max_v = max(verticalCuts[0], w - verticalCuts[-1])
        
        for i in range(1, len(horizontalCuts)):
            max_h = max(horizontalCuts[i] - horizontalCuts[i - 1], max_h)
        
        for i in range(1, len(verticalCuts)):
            max_v = max(verticalCuts[i] - verticalCuts[i - 1], max_v)
        
        return max_h * max_v % (1000000007)
    
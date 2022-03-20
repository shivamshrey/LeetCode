# 2211. Count Collisions on a Road
# https://leetcode.com/problems/count-collisions-on-a-road/

class Solution:
    def countCollisions(self, directions: str) -> int:
        x, y, result = 0, 0, 0
        for char in directions:
            if char == 'L':
                result += x
            else:
                x = 1
        
        for char in reversed(directions):
            if char == 'R':
                result += y
            else:
                y = 1
        
        return result
        
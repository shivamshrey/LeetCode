# 1762. Buildings With an Ocean View
# https://leetcode.com/problems/buildings-with-an-ocean-view/

# TC: O(n)
# SC: O(1)

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        result = []
        max_height = -1
        
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > max_height:
                max_height = heights[i]
                result.append(i)
            
        return result[::-1]
        
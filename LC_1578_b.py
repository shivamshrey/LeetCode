# 1578. Minimum Time to Make Rope Colorful
# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        result = 0
        cur_max = 0
        
        for i in range(len(neededTime)):
            if i > 0 and colors[i] != colors[i - 1]:
                cur_max = 0
            result += min(cur_max, neededTime[i])
            cur_max = max(cur_max, neededTime[i])
        
        return result        
    
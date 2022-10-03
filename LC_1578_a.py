# 1578. Minimum Time to Make Rope Colorful
# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        left = right = 0
        cur_total = cur_max = 0
        result = 0
        while right < len(colors):
            if colors[left] == colors[right]:
                cur_total += neededTime[right]
                cur_max = max(cur_max, neededTime[right])
            else:
                left = right
                result += cur_total - cur_max
                cur_total = neededTime[left]
                cur_max = neededTime[left]
            right += 1
        result += cur_total - cur_max
        return result
        
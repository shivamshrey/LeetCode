# 746. Min Cost Climbing Stairs

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [0] * (len(cost) + 1)
        
        for i in range(2, len(cost) + 1):
            down_one = cost[i - 1] + minCost[i - 1]
            down_two = cost[i - 2] + minCost[i - 2]
            minCost[i] = min(down_one, down_two)
        
        return minCost[-1]
    
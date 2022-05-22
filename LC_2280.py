# 2280. Minimum Lines to Represent a Line Chart
# https://leetcode.com/problems/minimum-lines-to-represent-a-line-chart/

class Solution:
    def minimumLines(self, stockPrices: List[List[int]]) -> int:
        if len(stockPrices) == 1: return 0
        
        result = 1
        stockPrices.sort()
        for i in range(1, len(stockPrices) - 1):
            x1, y1 = stockPrices[i - 1]
            x2, y2 = stockPrices[i]
            x3, y3 = stockPrices[i + 1]
            
            if (x2 - x1) * (y3 - y2) != (y2 - y1) * (x3 - x2):
                result += 1
        return result
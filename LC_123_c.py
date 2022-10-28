# 123. Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# TC: O(N * 2 * 3)
# SC: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        nnext = [[0] * 3 for _ in range(2)]
        cur = [[0] * 3 for _ in range(2)]
        
        # Base case: when i = n
        for j in range(2):
            for transaction in range(2):
                nnext[j][transaction] = 0
        
        # Base case: when transactions = 0
        for i in range(n):
            for buy_allowed in range(2):
                nnext[buy_allowed][0]
                
        for i in range(n - 1, -1, -1):
            for buy_allowed in range(2):
                for transaction in range(1, 3):
                    if buy_allowed == 1:
                        cur[buy_allowed][transaction] = max(-prices[i] + nnext[0][transaction],
                                                              nnext[1][transaction])
                    else:
                        cur[buy_allowed][transaction] = max(prices[i] + nnext[1][transaction - 1],
                                                              nnext[0][transaction])
            nnext = cur
        return nnext[1][2]
    
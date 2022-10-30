# 123. Best Time to Buy and Sell Stock III
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

# TC: O(N * 4)
# SC: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        nnext = [0] * 5
        cur  = [0] * 5
        
        for i in range(n - 1, -1, -1):
            for transaction in range(1, 5):
                if transaction % 2 == 0:   # buy allowed
                    cur[transaction] = max(-prices[i] + nnext[transaction - 1],
                                           nnext[transaction])
                else:                       # sell allowed
                    cur[transaction] = max(prices[i] + nnext[transaction - 1],
                                           nnext[transaction])
            nnext = cur
        return nnext[4]
    
# 188. Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# TC: O(N * K)
# SC: O(K)

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        nnext = [0] * (k * 2 + 1)
        cur  = [0] * (k * 2 + 1)
        
        for i in range(n - 1, -1, -1):
            for transaction in range(1, k * 2 + 1):
                if transaction % 2 == 0:   # buy allowed
                    cur[transaction] = max(-prices[i] + nnext[transaction - 1],
                                           nnext[transaction])
                else:                       # sell allowed
                    cur[transaction] = max(prices[i] + nnext[transaction - 1],
                                           nnext[transaction])
            nnext = cur
        return nnext[k * 2]
    
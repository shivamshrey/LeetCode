# 122. Best Time to Buy and Sell Stock II
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        nnext = [-1] * 2
        cur = [-1] * 2
        nnext[0] = nnext[1] = 0
        for i in range(n - 1, -1, -1):
            for buy_allowed in range(2):
                profit = 0

                if buy_allowed == 1:
                    profit = max(-prices[i] + nnext[0],    # buy
                                 nnext[1])                    # don't buy
                else:
                    profit = max(prices[i] + nnext[1],        # sell
                                 nnext[0])                # don't sell

                cur[buy_allowed] = profit
            nnext = cur

        return nnext[1]

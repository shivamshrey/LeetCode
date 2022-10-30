# 309. Best Time to Buy and Sell Stock with Cooldown
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

# TC: O(N)
# SC: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        cur = [0] * 2
        nnext1 = [0] * 2
        nnext2 = [0] * 2
        
        for i in range(n - 1, -1, -1):              
            cur[1] = max(-prices[i] + nnext1[0],    # buy
                         nnext1[1])                    # don't buy

            cur[0] = max(prices[i] + nnext2[1],        # sell
                         nnext1[0])                # don't sell

            nnext2 = nnext1[:]
            nnext1 = cur[:]
        return cur[1]
    
# 188. Best Time to Buy and Sell Stock IV
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

# TC: O(N * 2 * K)
# SC: O(K)

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        nnext = [[0] * (k + 1) for _ in range(2)]
        cur = [[0] * (k + 1) for _ in range(2)]
        
        # Base case: when i = n
        for j in range(2):
            for transaction in range(2):
                nnext[j][transaction] = 0
        
        # Base case: when transactions = 0
        for i in range(n):
            for buy_allowed in range(2):
                nnext[buy_allowed][0] = 0
                
        for i in range(n - 1, -1, -1):
            for buy_allowed in range(2):
                for transaction in range(1, k + 1):
                    if buy_allowed == 1:
                        cur[buy_allowed][transaction] = max(-prices[i] + nnext[0][transaction],
                                                            nnext[1][transaction])
                    else:
                        cur[buy_allowed][transaction] = max(prices[i] + nnext[1][transaction - 1],
                                                            nnext[0][transaction])
            nnext = cur
        return nnext[1][k]
    
    
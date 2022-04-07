# 441. Arranging Coins
# https://leetcode.com/problems/arranging-coins/

class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 1, n
        
        while low <= high:
            mid = (low + high) >> 1
            
            coins = mid * (mid + 1) // 2
            
            if coins > n:
                high = mid - 1
            elif coins < n:
                low = mid + 1
            else:
                return mid
        
        return high
    
# 1155. Number of Dice Rolls With Target Sum
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def helper(n, target):
            if target > k * n:
                return 0
            if n == 0: return target == 0
            if target < 0: return 0
            
            ways = 0
            for i in range(1, k + 1):
                ways += helper(n - 1, target - i)
            
            return ways
        
        return helper(n, target) % (10**9+7)
    
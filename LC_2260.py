# 2260. Minimum Consecutive Cards to Pick Up
# https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up/

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        result = float('inf')
        last_seen = dict()
        
        for i, val in enumerate(cards):
            if val in last_seen:
                result = min(result, i - last_seen[val] + 1)
            last_seen[val] = i
        
        return -1 if result == float('inf') else result
    
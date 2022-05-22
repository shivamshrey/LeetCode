# Maximum Bags With Full Capacity of Rocks
# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        diff = []
        for c, r in zip(capacity, rocks):
            diff.append(c - r)
        diff.sort()
        result = 0
        while result < len(capacity) and additionalRocks >= diff[result]:
            additionalRocks -= diff[result]
            result += 1
        
        return result
    
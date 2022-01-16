# 2139. Minimum Moves to Reach Target Score

# TC: O(log n)
# SC: O(1)
class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        while target > 1 and maxDoubles > 0:
            moves += 1 + target % 2
            maxDoubles -= 1
            target >>= 1
        return (target - 1) + moves
    
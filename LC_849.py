# 849. Maximize Distance to Closest Person

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        last = -1   # last index when seats[last] == 1
        result = 1
        n = len(seats)
        
        for i in range(n):
            if seats[i] == 1:
                if last == -1:
                    result = i
                else:
                    result = max(result, (i - last) // 2)
                last = i
        
        if seats[n - 1] == 0:
            result = max(result, n - 1 - last)
        
        return result
    
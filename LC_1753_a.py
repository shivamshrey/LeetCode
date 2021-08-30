# 1753. Maximum Score From Removing Stones

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        heap = [-a, -b, -c]
        heapq.heapify(heap)
        score = 0
        while True:
            x, y = heapq.heappop(heap), heapq.heappop(heap)
            if x == 0 or y == 0:
                break
            score += 1
            x, y = abs(x) - 1, abs(y) - 1
            heapq.heappush(heap, -x)
            heapq.heappush(heap, -y)
        
        return score
    
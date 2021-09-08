# 1792. Maximum Average Pass Ratio

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        heap = [(p / t - (p + 1) / (t + 1), p, t) for p, t in classes]
        heapify(heap)   # maxheapify
        
        while extraStudents:
            v, p, t = heapq.heappop(heap)
            p, t = p + 1, t + 1 # add extra students
            heapq.heappush(heap, (-(p + 1) / (t + 1) + p / t, p, t))    # push delta as if new student were to added into this for next iteration
            extraStudents -= 1
        
        return sum(p / t for v, p, t in heap) / len(heap)
    
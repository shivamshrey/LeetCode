# 1738. Find Kth Largest XOR Coordinate Value

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        heap = []   # minheap
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i != 0:
                    matrix[i][j] ^= matrix[i - 1][j]
                if j != 0:
                    matrix[i][j] ^= matrix[i][j - 1]
                if i != 0 and j != 0:
                    matrix[i][j] ^= matrix[i - 1][j- 1]
                
                heapq.heappush(heap, matrix[i][j])
                if len(heap) > k:
                    heapq.heappop(heap)
        
        return heap[0]
    
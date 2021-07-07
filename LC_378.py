# 378. Kth Smallest Element in a Sorted Matrix

# Time Complexity: let X = min(K, N); O(X + Klog(X))
# Space Complexity: O(X) occupied by the heap
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        heap = []
        
        for i in range(min(n, k)):
            heap.append((matrix[i][0], i, 0))
        heapify(heap)
        
        while k > 0:
            element, row, column = heappop(heap)
            if column < n - 1:
                heappush(heap, (matrix[row][column + 1], row, column + 1))
            k -= 1
        
        return element
    
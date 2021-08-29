# 1337. The K Weakest Rows in a Matrix

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []   # maxheap, stores [soldiers, i]
        
        for i, row in enumerate(mat):
            heapq.heappush(heap, [-self.countSoldiers(row), -i])
            
            if len(heap) > k:
                heapq.heappop(heap)
        
        result = []
        while heap:
            result.append(-heapq.heappop(heap)[1])
            
        return result[::-1]
        
    def countSoldiers(self, row):
        low, high = 0, len(row) - 1
        
        result = 0
        while low <= high:
            mid = low + (high - low) // 2
            if row[mid] == 1:
                result = mid + 1    # + 1 to store the count
                low = mid + 1
            else:
                high = mid - 1
        
        return result
    
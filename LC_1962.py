# 1962. Remove Stones to Minimize the Total

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-pile for pile in piles]
        heapq.heapify(heap) # max heapify
        
        while k > 0:
            max_pile = -heapq.heappop(heap)
            max_pile = max_pile - max_pile // 2
            heapq.heappush(heap, -max_pile)
            k -= 1
        
        return -sum(heap)
    
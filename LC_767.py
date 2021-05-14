# 767. Reorganize String

class Solution:
    def reorganizeString(self, S: str) -> str:
        hm = dict()
        for i in range(len(S)):
            hm[S[i]] = hm.get(S[i], 0) + 1

        heap = [(-freq, char) for char, freq in hm.items()]
        # Build max-heap based on frequency
        heapify(heap)

        result = ""
        prev_a, prev_b = 0, ""
        
        while heap:
            a, b = heappop(heap)
            result += b
            if prev_a < 0:
                heappush(heap, (prev_a, prev_b))
                
            a += 1
            prev_a, prev_b = a, b
            
        if len(result) != len(S):
            return ""
        
        return result
    
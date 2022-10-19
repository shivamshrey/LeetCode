# 692. Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/

# TC: O(N + klogN)
# SC: O(N)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_count = collections.Counter(words)
        heap = []   # maxheap
        for word, frequency in word_count.items():
            heap.append([-frequency, word])
            
        heapq.heapify(heap)
        
        result = []
        while k > 0:
            result.append(heapq.heappop(heap)[1])
            k -= 1
        
        return result

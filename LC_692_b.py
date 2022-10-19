# 692. Top K Frequent Words
# https://leetcode.com/problems/top-k-frequent-words/

# TC: O(N log K)
# SC: O(N + K)

class Pair:
    def __init__(self, word, count):
        self.word = word
        self.count = count
        
    def __lt__(self, pair):
        return self.count < pair.count or (self.count == pair.count and self.word > pair.word)

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counts = collections.Counter(words)
        heap = []
        for word, count in counts.items():
            heapq.heappush(heap, Pair(word, count))
            if len(heap) > k: heapq.heappop(heap)
        
        return [pair.word for pair in sorted(heap, reverse=True)]

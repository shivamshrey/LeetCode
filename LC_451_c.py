# 451. Sort Characters By Frequency

# n = string length, k = no. of unique characters
# TC: O(n) + O(n) + O(n) + O(k) + O(n) + O(n) = O(n)
# SC: O(n)
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        max_freq = max(counts.values())
        
        bucket = [[] for _ in range(max_freq + 1)]
        for c, i in counts.items():
            bucket[i].append(c)
        
        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for c in bucket[i]:
                result.append(c * i)
        
        return "".join(result)
    
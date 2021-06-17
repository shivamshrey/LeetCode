# 451. Sort Characters By Frequency

# n = string length, k = no. of unique characters
# TC: O(n) + O(k log k) + O(n) + O(n) = O(n + k log k)
# SC: O(k) + O(n) = O(n)
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = dict(sorted(Counter(s).items(), key=lambda item: -item[1]))
        result = []

        for key, value in counts.items():
            result.append(key * value)
        
        return "".join(result)
    
# 451. Sort Characters By Frequency

# n = string length, k = no. of unique characters
# TC: O(n) + O(k log k) + O(n) = O(n + k log k)
# SC: O(k) + O(n) = O(n)
class Solution:
    def frequencySort(self, s: str) -> str:
        counts = Counter(s)
        result = []

        for letter, frequency in counts.most_common():
            result.append(letter * frequency)
        
        return "".join(result)
    
# 1338. Reduce Array Size to The Half

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        half = n // 2
        hashmap = collections.Counter(arr)
        result = 0
        
        for num, frequency in hashmap.most_common():
            result += 1
            n -= frequency
            if n <= half:
                return result
            
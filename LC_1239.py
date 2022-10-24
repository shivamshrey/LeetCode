# 1239. Maximum Length of a Concatenated String with Unique Characters
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def backtrack(start, s):
            word = "".join(s)
            if len(word) != len(set(word)): return 0
            
            count = len(word)
            for i in range(start, len(arr)):
                count = max(count, backtrack(i + 1, s + [arr[i]]))
            return count
        
        return backtrack(0, [])
    
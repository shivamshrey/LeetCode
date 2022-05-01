# 2262. Total Appeal of A String
# https://leetcode.com/problems/total-appeal-of-a-string/

class Solution:
    def appealSum(self, s: str) -> int:
        last_seen_index = dict()
        result, count = 0, 0
        
        for i, c in enumerate(s):
            count += i - last_seen_index.get(c, -1)
            last_seen_index[c] = i
            result += count
        
        return result
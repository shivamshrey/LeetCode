# 2262. Total Appeal of A String
# https://leetcode.com/problems/total-appeal-of-a-string/

class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        last_seen_index = dict()
        ans = 0
        for i, c in enumerate(s):
            if c not in last_seen_index:
                ans += (i + 1) * (n - i)
            else:
                ans += (i - last_seen_index[c]) * (n - i)
            last_seen_index[c] = i
        
        return ans
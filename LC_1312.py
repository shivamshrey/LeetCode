# 1312. Minimum Insertion Steps to Make a String Palindrome
# https://leetcode.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/

class Solution:
    def minInsertions(self, s: str) -> int:
        def lps(s):
            def lcs(s, t):
                m, n = len(s), len(t)
                prev = [0] * (n + 1)
                for i in range(1, m + 1):
                    cur = [0] * (n + 1)
                    for j in range(1, n + 1):
                        if s[i - 1] == t[j - 1]:
                            cur[j] = 1 + prev[j - 1]
                        else:
                            cur[j] = max(cur[j - 1], prev[j])
                    prev = cur
                return prev[n]
            return lcs(s, s[::-1])
        return len(s) - lps(s)
    
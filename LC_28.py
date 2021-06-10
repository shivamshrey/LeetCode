# 28. Implement strStr()

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            match_found = True
            for j in range(m):
                if needle[j] != haystack[i + j]:
                    match_found = False
                    break
            if match_found:
                return i

        return -1

# 409. Longest Palindrome

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = [0] * 128
        for i in s:
            counts[ord(i)] += 1
        
        result = 0
        for count in counts:
            result += count // 2 * 2
            if result % 2 == 0 and count % 2 == 1:
                result += 1
        
        return result 
        
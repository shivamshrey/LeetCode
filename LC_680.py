# https://leetcode.com/problems/valid-palindrome-ii/
# 680. Valid Palindrome II

class Solution:
    def validPalindrome(self, s: str) -> bool:
        low, high, count = 0, len(s) - 1, 0
        
        while low < high:
            if s[low] != s[high]:
                return (self.__checkPalindrome(s, low, high - 1) or
                        self.__checkPalindrome(s, low + 1, high))
            low += 1
            high -= 1
        
        return True
        
    def __checkPalindrome(self, s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True
    
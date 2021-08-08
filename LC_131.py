# 131. Palindrome Partitioning

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        self.backtrack(0, [], result, s)
        return result
    
    def backtrack(self, start, cur, result, s):
        if start == len(s):
            result.append(list(cur))
            return
            
        for end in range(start, len(s)):
            if self.isPalindrome(s, start, end):
                cur.append(s[start:end + 1])
                self.backtrack(end + 1, cur, result, s)
                cur.pop()
        

    def isPalindrome(self, s, low, high):
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True
    
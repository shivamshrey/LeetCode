# 557. Reverse Words in a String III

class Solution:
    def reverseWords(self, s: str) -> str:
        start = 0
        end = 0
        result = ""
        while end < len(s):
            if s[end] == " ":
                result += self.reverseInRange(s, start, end - 1) + " "
                start = end + 1
            end += 1
        
        return result + self.reverseInRange(s, start, end - 1)
    
    def reverseInRange(self, s: str, start: int, end: int) -> str:
        result = ""
        for i in range(end, start - 1, -1):
            result += s[i]
        return result
        
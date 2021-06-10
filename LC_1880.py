# 1880. Check if Word Equals Summation of Two Words

class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        
        def numericSum(s: str) -> int:
            result = ""
            for ch in s:
                result += str(ord(ch) - ord('a'))
            return int(result)
        
        return numericSum(firstWord) + numericSum(secondWord) == numericSum(targetWord)
        
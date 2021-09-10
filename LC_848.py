# 848. Shifting Letters

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        for i in range(len(shifts) - 2, -1, -1):    # suffix sum
            shifts[i] += shifts[i + 1]
        
        result = []
        for i in range(len(s)):
            shift = (ord(s[i]) - ord('a') + shifts[i]) % 26
            result.append(chr(shift + ord('a')))
        
        return "".join(result)
    
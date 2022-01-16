# 2138. Divide a String Into Groups of Size k

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        i = 0
        while i + k <= len(s):
            result.append(s[i:i + k])
            i += k
        
        if i < len(s):
            remaining = len(s[i:])
            result.append(s[i:] + fill * (k - remaining))
        
        return result            
        
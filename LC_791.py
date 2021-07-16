# 791. Custom Sort String

class Solution:
    def customSortString(self, order: str, str: str) -> str:
        count = Counter(str)
        
        result = []
        
        for ch in order:
            if ch in count:
                result.append(ch * count.pop(ch))
        
        for ch, v in count.items():
            result.append(ch * v)
        
        return ''.join(result)
        
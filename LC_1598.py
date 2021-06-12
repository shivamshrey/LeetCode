# 1598. Crawler Log Folder

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for ch in logs:
            if ch == './' or (not stack and ch == '../'):
                continue
            if ch == '../':
                stack.pop()
            else:
                stack.append(ch)
        
        return len(stack)
    
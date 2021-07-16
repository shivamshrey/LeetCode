# 71. Simplify Path

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        
        for ch in path:
            if ch != '' and ch != '.' and ch != '..':
                stack.append(ch)
            elif ch == '..' and stack:
                stack.pop()
        
        return '/' + '/'.join(stack)

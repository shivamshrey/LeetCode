# 1209. Remove All Adjacent Duplicates in String II

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []  # stores list in the form [ch, count]
        
        for ch in s:
            if stack and stack[-1][0] == ch:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([ch, 1])
        
        return ''.join(ch * k for ch, k in stack)
    
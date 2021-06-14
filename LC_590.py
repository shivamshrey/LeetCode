# 590. N-ary Tree Postorder Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        stack = []
        result = []
        if root:
            stack.append(root)
        
        while stack:
            root = stack.pop()
            result.append(root.val)
            for child in root.children:
                stack.append(child)
    
        return result[::-1]
    
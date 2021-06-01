# 589. N-ary Tree Preorder Traversal

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if root == None:
            return []
            
        stack = []
        stack.append(root)
        result = []
        while stack:
            root = stack.pop()
            result.append(root.val)
            for child in reversed(root.children):
                stack.append(child)
                
        return result
    
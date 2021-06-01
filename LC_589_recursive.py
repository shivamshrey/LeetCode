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
        result = []
        
        def preorderUtil(root, result):
            if root == None:
                return
            result.append(root.val)
            for child in root.children:
                preorderUtil(child, result)
        
        preorderUtil(root, result)
        return result
    
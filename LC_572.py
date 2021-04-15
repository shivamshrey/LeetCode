# 572. Subtree of Another Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None:
            return False
        
        if self.isSameTree(s, t):
            return True
        
        return self.isSubtree(s.left, t) \
               or self.isSubtree(s.right, t)
        
    def isSameTree(self, s: TreeNode, t: TreeNode) -> bool:
        if s == None and t == None:
            return True
        
        if s == None or t == None:
            return False
        
        return s.val == t.val \
               and self.isSameTree(s.left, t.left) \
               and self.isSameTree(s.right, t.right)

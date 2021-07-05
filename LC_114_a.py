# 114. Flatten Binary Tree to Linked List

# TC: O(n)
# SC: O(n) for left-skewed tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # First, traverse in post order and keep changing links
        def flattenUtil(root: TreeNode) -> None:
            nonlocal prev
            if root == None:
                return
            flattenUtil(root.right)
            flattenUtil(root.left)
            root.right = prev
            root.left = None
            prev = root
        
        prev = None
        flattenUtil(root)
    
# 114. Flatten Binary Tree to Linked List

# TC: O(n)
# SC: O(1)

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
        while root:
            prev = root.left
            if prev:
                # find the rightmost node of left subtree
                while prev.right:
                    prev = prev.right
                # point the right of rightmost node of left subtree
                # to right of root
                prev.right = root.right
                # point the right to left
                root.right = root.left
                # point left to None
                root.left = None
            # move root to root.right in skewed resultant linked list
            root = root.right
    
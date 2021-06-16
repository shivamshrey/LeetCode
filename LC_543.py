# 543. Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def longest_path(root):
            nonlocal diameter
            if root == None:
                return 0
            
            left_path = longest_path(root.left)
            right_path = longest_path(root.right)
            
            diameter = max(diameter, left_path + right_path)
            
            return max(left_path, right_path) + 1
        
        diameter = 0
        longest_path(root)
        return diameter
    
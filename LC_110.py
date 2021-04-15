# 110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.isBalancedUtil(root) != -1
    
    def isBalancedUtil(self, root: TreeNode) -> int:
        '''Returns height if tree is balanced otherwise -1'''
        if root == None:
            return 0
        
        left_height = self.isBalancedUtil(root.left)
        if left_height == -1:
            return -1
        
        right_height = self.isBalancedUtil(root.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
        
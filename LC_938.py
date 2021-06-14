# 938. Range Sum of BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        stack = []
        stack.append(root)
        result = 0
        
        while stack:
            node = stack.pop()
            if low <= node.val <= high:
                result += node.val
            
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        
        return result
        
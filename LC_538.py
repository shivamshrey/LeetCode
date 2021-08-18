# 538. Convert BST to Greater Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse_inorder(root):
            if root:
                if root.right:
                    reverse_inorder(root.right)
                self.val = self.val + root.val
                root.val = self.val
                if root.left:
                    reverse_inorder(root.left)
        
        self.val = 0
        reverse_inorder(root)
        return root
    
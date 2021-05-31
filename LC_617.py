# 617. Merge Two Binary Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if root1 == None and root2 == None:
            return None
        
        root = TreeNode((root1.val if root1 else 0) + (root2.val if root2 else 0))
        root.left = self.mergeTrees(root1.left if root1 else None,
                                    root2.left if root2 else None)
        root.right = self.mergeTrees(root1.right if root1 else None,
                                     root2.right if root2 else None)
        return root
    
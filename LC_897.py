# 897. Increasing Order Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            if root == None:
                return None
            inorder(root.left)
            root.left = None
            self.cur.right = root
            self.cur = root
            inorder(root.right)
        
        new_root = self.cur = TreeNode()
        inorder(root)
        return new_root.right
        
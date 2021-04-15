# 236. Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == None or root == p or root == q:
            return root

        lca_left = self.lowestCommonAncestor(root.left, p, q)
        lca_right = self.lowestCommonAncestor(root.right, p, q)

        # if one subtree has p and the other has q
        # then current root is the lca
        if lca_left != None and lca_right != None:
            return root

        # if neither p nor q is present in either subtree
        if lca_left == None and lca_right == None:
            return None

        if lca_left != None:
            return lca_left
        else:
            return lca_right
        
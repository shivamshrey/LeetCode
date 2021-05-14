# 98. Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        min_val = -sys.maxsize - 1
        max_val = sys.maxsize

        def isValidBSTUtil(root, min_val, max_val):
            if root == None:
                return True

            return min_val < root.val < max_val \
                and isValidBSTUtil(root.left, min_val, root.val) \
                    and isValidBSTUtil(root.right, root.val, max_val)

        return isValidBSTUtil(root, min_val, max_val)
    
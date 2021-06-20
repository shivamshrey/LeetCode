# 530. Minimum Absolute Difference in BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inorder(root):
            if root == None:
                return
            inorder(root.left)
            self.min_diff = min(self.min_diff, root.val - self.prev)
            self.prev = root.val
            inorder(root.right)
        
        self.min_diff = math.inf
        self.prev = -math.inf
        inorder(root)
        return self.min_diff
    
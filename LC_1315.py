# 1315. Sum of Nodes with Even-Valued Grandparent

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode, parent=1, grandparent=1) -> int:
        return self.sumEvenGrandparent(root.left, root.val, parent) \
            + self.sumEvenGrandparent(root.right, root.val, parent) \
            + root.val * (1 - grandparent % 2) if root else 0
    
# 230. Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 0
        result = 0
        
        def kthSmallestUtil(root: TreeNode, k: int) -> int:
            nonlocal count, result
            
            if root:
                kthSmallestUtil(root.left, k)
                count += 1
                if count == k:
                    result = root.val
                    return
                kthSmallestUtil(root.right, k)
                
        kthSmallestUtil(root, k)
        return result
        
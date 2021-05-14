# 98. Validate Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        prev = -sys.maxsize - 1
        
        def isValidBSTUtil(root: TreeNode) -> bool:
            nonlocal prev
            
            if root == None:
                return True
            
            if not isValidBSTUtil(root.left):
                return False
            
            if prev >= root.val:
                return False
            
            prev = root.val
            
            return isValidBSTUtil(root.right)

            
        return isValidBSTUtil(root)
    
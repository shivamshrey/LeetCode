# 99. Recover Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = None
        first = None
        second = None
        
        def findNodes(root: TreeNode) -> None:
            nonlocal prev, first, second
            
            if root == None:
                return
            
            findNodes(root.left)
            
            if prev != None and prev.val >= root.val:
                if first == None:
                    first = prev
                second = root
                
            prev = root
            
            findNodes(root.right)
                
        findNodes(root)
        
        first.val, second.val = second.val, first.val
        
# 144. Binary Tree Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        preorder = []
        
        if root:
            stack.append(root)
        
        while stack:
            cur = stack.pop()
            preorder.append(cur.val)
            
            if cur.right:
                stack.append(cur.right)
            if cur.left:
                stack.append(cur.left)
            
        return preorder
    
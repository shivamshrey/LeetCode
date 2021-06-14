# 1469. Find All The Lonely Nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        stack = []
        stack.append(root)
        result = []
        
        while stack:
            node = stack.pop()
            
            if node.left and not node.right:
                result.append(node.left.val)
            if node.right and not node.left:
                result.append(node.right.val)
            
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
            
        return result
        
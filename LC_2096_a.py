# 2096. Step-By-Step Directions From a Binary Tree Node to Another
# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        def lca(root):
            if not root or root.val in (startValue, destValue): return root
            lca_left, lca_right = lca(root.left), lca(root.right)
            return root if lca_left and lca_right else lca_left or lca_right
        
        lca_root = lca(root)
        start_path, dest_path = "", ""
        
        stack = [(lca_root, "")]
        while stack:    # do dfs, e.g. post order
            node, path = stack.pop()
            if node.val == startValue: start_path = path
            elif node.val == destValue: dest_path = path
            if node.left: stack.append((node.left, path + 'L'))
            if node.right: stack.append((node.right, path + 'R'))
            
        return "U" * len(start_path) + dest_path

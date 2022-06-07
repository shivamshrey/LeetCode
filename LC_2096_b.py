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
        def find_path(root: TreeNode, val: int, path: List[str]) -> bool:
            if root.val == val: return True
            if root.left and find_path(root.left, val, path):
                path += 'L'
            elif root.right and find_path(root.right, val, path):
                path += 'R'
            return path
        
        start_path, dest_path = [], []
        find_path(root, startValue, start_path)
        find_path(root, destValue, dest_path)
        
        while start_path and dest_path and start_path[-1] == dest_path[-1]:
            start_path.pop()
            dest_path.pop()
        
        return "".join("U" * len(start_path)) + "".join(reversed(dest_path))

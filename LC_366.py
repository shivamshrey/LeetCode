# 366. Find Leaves of Binary Tree
# https://leetcode.com/problems/find-leaves-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, height):
            if not root: return height
            
            left = dfs(root.left, height)
            right = dfs(root.right, height)
            height = max(left, right) + 1
            heights[height].append(root.val)
            return height

        heights = collections.defaultdict(list)
        dfs(root, 0)
        
        return heights.values()

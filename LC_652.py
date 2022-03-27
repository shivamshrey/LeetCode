# 652. Find Duplicate Subtrees
# https://leetcode.com/problems/find-duplicate-subtrees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        def dfs(root):  # preorder or postorder works
            if not root:
                return "null"
            structure = f"{root.val},{dfs(root.left)},{dfs(root.right)}"
            nodes[structure].append(root)
            return structure
        
        nodes = collections.defaultdict(list)   # structure -> list of nodes
        dfs(root)
        
        return [nodes_list[0] for nodes_list in nodes.values() if len(nodes_list) > 1]

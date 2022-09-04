# 987. Vertical Order Traversal of a Binary Tree
# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# TC: O(N log (N / k)) where k is width of the tree
# SC: O(N)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        col_table = collections.defaultdict(list)
        queue = collections.deque([(root, 0, 0)])
        
        min_col = max_col = 0
        
        while queue:
            node, row, col = queue.popleft()
            col_table[col].append((row, node.val))
            
            min_col = min(min_col, col)
            max_col = max(max_col, col)
            
            if node.left: queue.append((node.left, row + 1, col - 1))
            if node.right: queue.append((node.right, row + 1, col + 1))
            
        result = []
        for col in range(min_col, max_col + 1):
            result.append([val for key, val in sorted(col_table[col])])
            
        return result
    
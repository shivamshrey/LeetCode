# 314. Binary Tree Vertical Order Traversal
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/

# TC: O(n)
# SC: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        
        hashmap = collections.defaultdict(list)    # distance from root node -> node.val
        queue = collections.deque()
        
        min_distance, max_distance = 0, 0
        
        queue.append((root, 0))
        
        while queue:
            node, distance = queue.popleft()
            min_distance = min(min_distance, distance)
            max_distance = max(max_distance, distance)
            
            hashmap[distance].append(node.val)
            
            if node.left:
                queue.append((node.left, distance - 1))
            if node.right:
                queue.append((node.right, distance + 1))
            
        
        return [hashmap[distance] for distance in range(min_distance, max_distance + 1)]

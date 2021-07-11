# 426. Convert Binary Search Tree to Sorted Doubly Linked List

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root == None:
            return
        dummy = TreeNode()
        tail = dummy
        
        # Perform inorder traversal
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            
            # Build the linked list
            tail.right = cur
            cur.left = tail
            tail = tail.right
            
            cur = cur.right
        
        # make it circular
        # by pointing head.left to tail
        # and tail.right to head
        tail.right = dummy.right
        dummy.right.left = tail
        
        return dummy.right
        
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
        if not root:
            return None
        stack = []
        cur = root
        dummy = Node()
        tail = dummy
        
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            
            new_node = Node(cur.val)
            tail.right = new_node
            new_node.left = tail
            tail = new_node
            
            cur = cur.right
        
        head = dummy.right
        tail.right = head
        head.left = tail
        
        return head
    
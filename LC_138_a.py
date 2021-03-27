"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# TC: O(n)
# SC: O(n)

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:
            return head
        
        hm = dict()
        cur = head
        
        while cur != None:
            hm[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur != None:
            clone_cur = hm[cur]
            clone_cur.next = hm.get(cur.next, None)
            clone_cur.random = hm.get(cur.random, None)
            cur = cur.next
        clone_head = hm[head]
        
        return clone_head
    

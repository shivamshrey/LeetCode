# 993. Cousins in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        found_x = found_y = False
        
        queue = deque()
        queue.append(root)
        parent = None
        
        while queue:
            size = len(queue)
            # set found_x and found_y as False
            # before processing each level
            found_x = found_y = False
            
            for i in range(size):
                cur = queue.popleft()
                if cur.val == x:
                    found_x = True
                if cur.val == y:
                    found_y = True
                
                # return False for siblings
                if cur.left and cur.right:
                    # return False if left child is x and right child is y
                    if cur.left.val == x and cur.right.val == y:
                        return False
                    # return False if right child is x and left child is y
                    if cur.right.val == x and cur.left.val == y:
                        return False
                
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            # After processing a level
            # return True if both x and y are found
            # in the current level
            if found_x and found_y:
                return True
            # return False if only one of them is found
            # in the current level
            elif found_x or found_y:
                return False
        
        # Return False if x and y are not present at all
        return False            
        
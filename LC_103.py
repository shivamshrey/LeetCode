# 103. Binary Tree Zigzag Level Order Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root == None:
            return []
        
        stack1 = []
        stack2 = []
        result = []
        
        stack1.append(root)
        
        while stack1 or stack2:
            temp = []
            while stack1:
                cur = stack1.pop()
                temp.append(cur.val)
                if cur.left:
                    stack2.append(cur.left)
                if cur.right:
                    stack2.append(cur.right)
            
            if temp:
                result.append(temp)
            temp = []
            
            # add children of popped nodes from stack2 in reverse order to stack1
            while stack2:
                cur = stack2.pop()
                temp.append(cur.val)
                if cur.right:
                    stack1.append(cur.right)
                if cur.left:
                    stack1.append(cur.left)
            
            if temp:
                result.append(temp)
        
        return result               
        
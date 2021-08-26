# 449. Serialize and Deserialize BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        def helper(root):
            if root:
                data.append(root.val)
                helper(root.left)
                helper(root.right)
        
        data = []
        helper(root)
        return ' '.join(str(val) for val in data)

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        def helper(queue, low, high):
            if queue and low < queue[0] < high:
                val = queue.popleft()
                root = TreeNode(val)
                root.left = helper(queue, low, val)
                root.right = helper(queue, val, high)
                return root
        
        queue = collections.deque(int(val) for val in data.split())
        
        return helper(queue, -float('inf'), float('inf'))

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans

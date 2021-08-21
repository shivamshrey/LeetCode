# 894. All Possible Full Binary Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    memo = {0: [], 1: [TreeNode(0)]}
    
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n not in self.memo:
            result = []
            
            for i in range(1, n, 2):
                left_trees = self.allPossibleFBT(i)
                right_trees = self.allPossibleFBT(n - i - 1)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(0)
                        root.left = left
                        root.right = right
                        result.append(root)
                self.memo[n] = result

        return self.memo[n]
        
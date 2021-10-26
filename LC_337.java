// 337. House Robber III

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int rob(TreeNode root) {
        return robUtil(root, new HashMap<>());
    }
    
    public int robUtil(TreeNode root, Map<TreeNode, Integer> cache) {
        if (root == null)
            return 0;
        
        if (cache.containsKey(root))
            return cache.get(root);

        int choose = root.val;  // choose the current node
        if (root.left != null)
            choose += robUtil(root.left.left, cache) + robUtil(root.left.right, cache);
        if (root.right != null)
            choose += robUtil(root.right.left, cache) + robUtil(root.right.right, cache);

        int dontChoose = robUtil(root.left, cache) + robUtil(root.right, cache);  // not choosing the current node
        
        int result = Math.max(choose, dontChoose);  // getting the max

        cache.put(root, result);
        return result;
    }
}

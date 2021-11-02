// 297. Serialize and Deserialize Binary Tree

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {

    // Encodes a tree to a single string.
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        serializeUtil(root, sb);
        return sb.toString();
    }
    
    private void serializeUtil(TreeNode root, StringBuilder sb) {
        if (root == null) {
            sb.append("null").append(" ");
            return;
        }
        sb.append(String.valueOf(root.val)).append(" ");
        serializeUtil(root.left, sb);
        serializeUtil(root.right, sb);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        Queue<String> queue = new LinkedList<>(Arrays.asList(data.split(" ")));
        return deserializeUtil(queue);
    }
    
    private TreeNode deserializeUtil(Queue<String> queue) {
        String val = queue.poll();
        if (val.equals("null"))
            return null;
        
        TreeNode node = new TreeNode(Integer.valueOf(val));
        node.left = deserializeUtil(queue);
        node.right = deserializeUtil(queue);
        return node;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec ser = new Codec();
// Codec deser = new Codec();
// TreeNode ans = deser.deserialize(ser.serialize(root));
